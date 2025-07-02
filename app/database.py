import motor.motor_asyncio
from os import getenv
from dotenv import load_dotenv

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(getenv("MONGO_URI"))
db = client["secureFileDB"]
