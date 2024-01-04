from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

templates = Jinja2Templates(directory="templates/")

@router.get("/buttons", response_class=HTMLResponse)    # 펑션 호출 방식
async def buttons(request:Request) :
    return templates.TemplateResponse(name="gadgets/buttons.html"
                                      , context={"request":request})
    
@router.get("/cards")
# request = Request(query_parameters)
async def cards(request:Request) :
    # request.query_params
    # QueryParams('name=myungjunkim&email=sweet.mjkim%40gmail.com')
    # dict(request.query_params)
    # {'name': 'myungjunkim', 'email': 'sweet.mjkim@gmail.com'}
    return templates.TemplateResponse(name="gadgets/cards.html"
                                      , context={"request":request})
    
@router.post("/cards")
async def cards_post(request:Request) :
    # request.query_params
    # QueryParams('')
    # await request.form()
    # FormData([('name', 'myungjunkim'), ('email', 'sweet.mjkim@gmail.com')])
    # dict(await request.form())
    # {'name': 'myungjunkim', 'email': 'sweet.mjkim@gmail.com'}
    # form_datas = await request.form()
    # dict(form_datas)
    return templates.TemplateResponse(name="gadgets/cards.html"
                                      , context={"request":request})
    
@router.get("/colors", response_class=HTMLResponse)
async def colors(request:Request) :
    return templates.TemplateResponse(name="gadgets/colors.html"
                                      , context={"request":request})
    
@router.get("/containers", response_class=HTMLResponse)
async def containers(request:Request) :
    return templates.TemplateResponse(name="gadgets/containers.html"
                                      , context={"request":request})
    