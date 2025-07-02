from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.database import db
import os
from app.utils.auth import create_token
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from os import getenv

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
UPLOAD_DIR = "app/storage/uploaded_files"

ALLOWED = ["pptx", "docx", "xlsx"]

def validate_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
        return payload
    except JWTError:
        raise HTTPException(403, detail="Invalid token")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), user=Depends(validate_user)):
    if user["role"] != "ops":
        raise HTTPException(403, detail="Only Ops User allowed")
    ext = file.filename.split(".")[-1]
    if ext not in ALLOWED:
        raise HTTPException(400, detail="Invalid file type")
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    await db.files.insert_one({"filename": file.filename, "uploader": user["sub"]})
    return {"message": "Uploaded"}
