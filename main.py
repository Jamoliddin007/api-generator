from fastapi import FastAPI, HTTPException, Response, Depends
from fastapi.responses import FileResponse, PlainTextResponse
from sqlalchemy.orm import Session
from slugify import slugify

from models.user_input import FieldDefinition, APIGenerateRequest
from generators.fastapi_builder import generate_fastapi_code
from generators.generate_and_save import save_code_to_file
from database.models import GeneratedProject, ProjectField
from project_root.dependencies import get_db
from schemas.schemas import ProjectOut

app = FastAPI()

# 1. Kodni faqat string sifatida qaytaradi
@app.post("/generate/", response_class=Response, responses={200: {"content": {"text/plain": {}}}})
def generate_code(request: APIGenerateRequest):
    try:
        code = generate_fastapi_code(request.fields)
        return Response(content=code, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Kodni .py fayl qilib yuklab beradi
@app.post("/generate-file/")
def generate_and_save(request: APIGenerateRequest):
    try:
        code = generate_fastapi_code(request.fields)
        file_path = save_code_to_file(code)
        return FileResponse(file_path, filename="generated_api.py", media_type="text/x-python")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Kodni generatsiya + faylga yozish + DBga yozish
@app.post("/generate-and-save-to-db/")
def generate_and_save_all(request: APIGenerateRequest, db: Session = Depends(get_db)):
    try:
        code = generate_fastapi_code(request.fields)
        file_path = save_code_to_file(code)
        slug = slugify(request.project_name)

        project = GeneratedProject(
            name=request.project_name,
            slug=slug,
            file_path=file_path
        )
        db.add(project)
        db.commit()
        db.refresh(project)

        for field in request.fields:
            db.add(ProjectField(
                project_id=project.id,
                name=field.name,
                type=field.type
            ))
        db.commit()

        return {
            "message": "API created and saved to DB successfully",
            "slug": slug,
            "file_path": file_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/projects/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    projects = db.query(GeneratedProject).order_by(GeneratedProject.created_at.desc()).all()
    return projects