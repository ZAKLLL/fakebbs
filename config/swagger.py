from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OpenAPI
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/docs", response_class=HTMLResponse)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API documentation")

@router.get("/openapi.json", response_model=OpenAPI)
async def get_openapi_endpoint():
    return router.openapi()