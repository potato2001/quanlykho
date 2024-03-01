from fastapi import Depends, FastAPI, Request, Form,status,Header,APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import exists
import base64
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from datetime import date
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT,decodeJWT,refresh_access_token
from model import CategorySchema
from database import SessionLocal, engine
import model

router = APIRouter()  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Thêm loại
@router.post("/create_category",dependencies=[Depends(JWTBearer())], summary="Tạo loại sản phẩm")
async def create_category(
    db: Session = Depends(get_database_session),
    CategoryName: str = Form(...),
):
    Category_exists = db.query(exists().where(CategorySchema.CategoryName == CategoryName)).scalar()
    if Category_exists:
        return {"data": "Loại sản phẩm đã tồn tại!"}
    CategorySchema = CategorySchema(categoryName = CategoryName)
    db.add(CategorySchema)
    db.commit()
    db.refresh(CategorySchema)
    return {
        "data:" "Tạo loại sản phẩm thành công!"
    }

# Sủa loại sản phẩm
@router.post("/update_category",dependencies=[Depends(JWTBearer())], summary="Sửa loại sản phẩm")
async def update_category(
    db: Session = Depends(get_database_session),
    CategoryName: str = Form(...),
):
    Category_exists = db.query(exists().where(CategorySchema.CategoryName == CategoryName)).scalar()
    Category = db.query(CategorySchema).get(CategoryName)
    if Category_exists:
        print(Category)
        Category.CategoryName = CategoryName
        db.commit()
        db.refresh(Category)
        return {
            "data": "Thông tin sản phẩm đã được cập nhật!"
        }
    else:
        return JSONResponse(status_code=400, content={"message": "Không có thông tin loại sản phẩm!"})

#Xóa loại sản phẩm
@router.delete("/delete_category",dependencies=[Depends(JWTBearer())], summary="Xóa loại sản phẩm")
async def delete_category(
    db: Session = Depends(get_database_session),
    CategoryID: int = Form(...)
):
    Category_exists = db.query(exists().where(CategorySchema.CategoryID == CategoryID)).scalar()
    if Category_exists:
        Category = db.query(CategorySchema).get(CategoryID)
        Category.HasBeenDeleted=1
        # db.delete(product)
        db.commit()
        db.refresh(Category)

        return{
         "data": "Xóa loại sản phẩm thành công!" 
        }
    else:
        return JSONResponse(status_code=400, content={"message": "Không tồn tại loại sản phẩm!"})
    
#Lấy tất cả loại sản phẩm
@router.get("/category", summary="Lấy tất cả loại sản phẩm")
def get_category(
    db: Session = Depends(get_database_session),
):
    Category = (
    db.query(CategorySchema)
    .all()
    )
    print(Category)
    result = []
    for Category in Category:
        result.append(
            {   
              Category
            }
        )
    return {"data": result}

