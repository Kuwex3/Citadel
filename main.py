from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()
    
@app.get("/full_files")
async def file_names(pswd: str):
    if pswd == "hashpass":
        return {"access"}

@app.get("/file/{name}")
async def get_file(name: str):
    return FileResponse(f"./public_files/{name}", filename=f"{name}")

@app.post("/send_file")
async def send_file(file: UploadFile):
    data = file.file.read().decode(encoding="UTF-8")