from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 Form /users/insert -> users/inserts.html
@router.get("/inserts")    # 주로 2단계까지만 연결
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={"request":request})

# 회원 가입 Login /users/insert -> users/login.html
@router.post("/logins")    # 주로 2단계까지만 연결
async def insert(request:Request):
    dict_details = dict(request.query_params)
    print(dict_details)
    return templates.TemplateResponse(name="users/logins.html"
                                      , context={"request":request})

# 회원 리스트 /users/list -> users/lists.html
@router.get("/list")
async def insert(request:Request):
    dict_details = dict(request.query_params)
    print(dict_details)
    return templates.TemplateResponse(name="users/lists.html"
                                      , context={"request":request})
    
# 회원 상세정보 /users/read -> users/reads.html
# path parameters : /users/read/id or /users/read/uniqe_name
@router.get("/read/{object_id}")
async def insert(request:Request, object_id):
    dict_details = dict(await request.form())
    print(dict_details)
    return templates.TemplateResponse(name="users/reads.html"
                                      , context={"request":request})
    
# 회원 리스트 /users/list -> users/lists.html
@router.post("/list")
async def insert(request:Request):
    dict_details = dict(request.query_params)
    print(dict_details)
    return templates.TemplateResponse(name="users/lists.html"
                                      , context={"request":request})