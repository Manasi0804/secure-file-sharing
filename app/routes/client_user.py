from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.utils.encryption import encrypt_id, decrypt_id
from app.database import db
from jose import jwt
from os import getenv

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
    return payload

@router.get("/list-files")
async def list_files(user=Depends(get_current_user)):
    if user["role"] != "client":
        raise HTTPException(403, detail="Only clients allowed")
    files = await db.files.find().to_list(100)
    return {"files": [f["filename"] for f in files]}

@router.get("/download-file/{file_name}")
async def generate_download(file_name: str, user=Depends(get_current_user)):
    if user["role"] != "client":
        raise HTTPException(403)
    encrypted = encrypt_id(file_name)
    return {"download-link": f"/client/secure-download/{encrypted}", "message": "success"}

@router.get("/secure-download/{token}")
async def secure_download(token: str, user=Depends(get_current_user)):
    if user["role"] != "client":
        raise HTTPException(403)
    try:
        filename = decrypt_id(token)
    except:
        raise HTTPException(400, detail="Invalid token")
    return {"message": "download allowed", "filename": filename}
