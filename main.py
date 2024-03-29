from fastapi import FastAPI

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from routes.homes import router as event_router
from routes.gadgets import router as gadgets
from routes.positionings import router as positionings
from routes.users import router as users_router

app.include_router(event_router, prefix="/homes")
app.include_router(gadgets, prefix="/gadgets")
app.include_router(positionings, prefix="/positionings")
app.include_router(users_router, prefix="/users")

from fastapi import Request
from fastapi.templating import Jinja2Templates
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@app.get("/index")
async def index(request:Request):
    # return {"message": "gocolab World!"}
    # html 틀로 호출
    return templates.TemplateResponse("index.html"
                                      ,{'request':request})
    
@app.get("/")
async def root(request:Request):
    # return {"message": "gocolab World!"}
    # html 틀로 호출
    return templates.TemplateResponse("main.html"
                                      ,{'request':request})