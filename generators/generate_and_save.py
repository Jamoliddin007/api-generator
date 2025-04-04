import uuid
from pathlib import Path

def save_code_to_file(code: str, base_dir="generated_apis") -> str:
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    file_name = f"{uuid.uuid4().hex}.py"
    file_path = Path(base_dir) / file_name
    file_path.write_text(code)
    return str(file_path)
