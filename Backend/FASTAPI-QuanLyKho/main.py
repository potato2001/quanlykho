from fastapi import Depends, FastAPI, Request, Form,status,Header,UploadFile,File
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import exists
import base64
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from datetime import date
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT,decodeJWT
from model import UserSchema
from database import SessionLocal, engine
from Routers import login,user,category
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",  # Adjust this based on your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Người dùng
app.include_router(login.router, tags=['Login Controller'], prefix='')
app.include_router(user.router, tags=['User Controller'], prefix='')

#Sản phẩm
# app.include_router(products.router, tags=['Products Controller'], prefix='')
app.include_router(category.router, tags=['Category Controller'], prefix='')

#Nhà cung cấp
# app.include_router(suppliers.router, tags=['Suppiler Controller'], prefix='')
# app.include_router(courseClass.router, tags=['Class Controller'], prefix='')
# app.include_router(exam.router, tags=['Exam Controller'], prefix='')
# app.include_router(studentExam.router, tags=['Student Exam Controller'], prefix='')
# app.include_router(grade.router, tags=['Grade Controller'], prefix='')
# app.include_router(bill.router, tags=['Bill Controller'], prefix='')

# Đơn hàng
# app.include_router(orders.router, tags=['Orders Controller'], prefix='')

