from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import PlainTextResponse, FileResponse
from models.user_input import FieldDefinition, APIGenerateRequest
from generators.fastapi_builder import generate_fastapi_code
from generators.generate_and_save import save_code_to_file



app = FastAPI()


@app.post("/generate/", response_class = Response, responses = {200: {"content": {"text/plain": {}}}})
def generate_code(request:APIGenerateRequest):
    try:
        code = generate_fastapi_code(request.fields)
        return Response(content=code, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-file/")
def generate_and_save(request: APIGenerateRequest):
    try:
        code = generate_fastapi_code(request.fields)
        file_path = save_code_to_file(code)
        return FileResponse(file_path, filename="generated_api.py", media_type="text/x-python")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
