from fastapi import FastAPI
from starlette.responses import RedirectResponse
import yaml

from adupangarai.v0.api.routes import router

app = FastAPI()

# Include routes
app.include_router(router)


# Load external OpenAPI YAML
def custom_openapi():
    with open("adupangarai/v0/spec/api.yaml", "r") as file:
        openapi_schema = yaml.safe_load(file)

    return openapi_schema

# Assign the custom OpenAPI schema generator
app.openapi_schema = None  # Cache the schema
def custom_openapi_method():
    if not app.openapi_schema:
        app.openapi_schema = custom_openapi()
    return app.openapi_schema

app.openapi = custom_openapi_method


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")