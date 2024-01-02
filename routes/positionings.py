from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

templates = Jinja2Templates(directory="templates/positionings/")

@router.get("/forms")
async def forms(request:Request) :
    return templates.TemplateResponse(name="forms.html"
                                      , context={"request":request})
    
@router.get("/glrids")
async def glrids(request:Request) :
    return templates.TemplateResponse(name="glrids.html"
                                      , context={"request":request})
    
@router.get("/standards")
async def standards(request:Request) :
    return templates.TemplateResponse(name="standards.html"
                                      , context={"request":request})
    
@router.get("/tables")
async def tables(request:Request) :
    return templates.TemplateResponse(name="tables.html"
                                      , context={"request":request})