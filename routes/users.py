from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 form /users/insert -> users/inserts.html
@router.get("/form")    # 주로 2단계까지만 연결
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={"request":request})

# 회원 가입 /users/insert -> users/login.html
@router.get("/inserts")    # 주로 2단계까지만 연결
async def insert(request:Request):
    pass    # biz
    return templates.TemplateResponse(name="users/logins.html"
                                      , context={"request":request})
    