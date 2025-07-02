from fastapi import APIRouter, HTTPException
from app.database import db
from app.utils.auth import hash_password, verify_password, create_token
from app.models import User

router = APIRouter()

@router.post("/signup/client")
async def signup(user: User):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(400, detail="User exists")
    await db.users.insert_one(user_dict)
    return {"message": "Signed up", "encrypted_url": create_token({"sub": user.email})}

@router.post("/login")
async def login(user: User):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(401, detail="Invalid credentials")
    return {"token": create_token({"sub": user.email, "role": db_user["role"]})}

