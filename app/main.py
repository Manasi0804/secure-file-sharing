from fastapi import FastAPI
from app.routes import auth, ops_user, client_user
from fastapi import FastAPI
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi


app = FastAPI(title="Secure File Sharing System")


app.include_router(auth.router, prefix="/auth")
app.include_router(ops_user.router, prefix="/ops")
app.include_router(client_user.router, prefix="/client")
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Secure File Sharing System",
        version="1.0.0",
        description="Paste your Bearer token in the Authorize dialog: Bearer <your-token>",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

