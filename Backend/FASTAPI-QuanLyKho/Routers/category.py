from fastapi import Depends, FastAPI, Request, Form,status,Header,APIRouter,HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import exists
import base64
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from datetime import date
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT,decodeJWT,refresh_access_token
from model import Category
from database import SessionLocal, engine
from schema import CategorySchema,MultipleCategoriesSchema,CategoryUpdateSchema
import model
from typing import List

router = APIRouter()  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Thêm loại
@router.post("/create_category", summary="Tạo loại sản phẩm")
async def create_category(
    categorySchema: CategorySchema,
    db: Session = Depends(get_database_session),
):
    category_exists = db.query(exists().where(Category.CategoryName == categorySchema.CategoryName)).scalar()
    if category_exists:
        return {"data": "Sản phẩm đã tồn tại!"}

    # Create a new ProductSchema instance and add it to the database
    new_category = Category(
        CategoryName=categorySchema.CategoryName,
        HasBeenDeleted=categorySchema.HasBeenDeleted,
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return categorySchema

# Sủa loại sản phẩm
@router.put("/update_category/{category_id}", summary="Cập nhật loại sản phẩm")
async def update_product(
    category_id: str,
    category_update: CategorySchema,
    db: Session = Depends(get_database_session),
):
    # Check if the product with the given ProductID exists
    existing_category = db.query(Category).filter(Category.CategoryID == category_id).first()
    if not existing_category:
        raise HTTPException(status_code=404, detail="Loại sản phẩm không tồn tại!")

    # Update the product fields with the new values
    existing_category.CategoryName = category_update.CategoryName
    existing_category.HasBeenDeleted = category_update.HasBeenDeleted
  
    # Commit the changes to the database
    db.commit()
    db.refresh(existing_category)

    return {"data": "Thông tin loại sản phẩm đã được cập nhật thành công!"}
@router.post("/create_categories", summary="Tạo nhiều loại sản phẩm")
async def create_categories(
    categories_schema: MultipleCategoriesSchema,
    db: Session = Depends(get_database_session),
):
    # List to store any duplicate category names
    duplicates = []

    for category in categories_schema.categories:
        category_exists = db.query(exists().where(Category.CategoryName == category.CategoryName)).scalar()
        if category_exists:
            duplicates.append(category.CategoryName)
        else:
            # Create a new Category instance and add it to the database
            new_category = Category(
                CategoryName=category.CategoryName,
                HasBeenDeleted=category.HasBeenDeleted,
            )
            db.add(new_category)

    db.commit()

    if duplicates:
        return {"data": f"Sản phẩm đã tồn tại: {', '.join(duplicates)}"}

    return {"data": "Tạo loại sản phẩm thành công"}
#Cập nhật nhiều loại sản phẩm
@router.put("/update_categories", summary="Cập nhật nhiều loại sản phẩm")
async def update_categories(
    categories_update: List[CategoryUpdateSchema],
    db: Session = Depends(get_database_session),
):
    duplicates = []

    for category_update in categories_update:
        # Check if the category with the given CategoryID exists
        existing_category = db.query(Category).filter(Category.CategoryID == category_update.CategoryID).first()
        if not existing_category:
            raise HTTPException(status_code=404, detail=f"Loại sản phẩm có ID {category_update.CategoryID} không tồn tại!")

        # Check for duplicate CategoryName
        if category_update.CategoryName != existing_category.CategoryName:
            category_exists = db.query(exists().where(Category.CategoryName == category_update.CategoryName)).scalar()
            if category_exists:
                duplicates.append(category_update.CategoryName)

        # Update the category fields with the new values
        existing_category.CategoryName = category_update.CategoryName
        existing_category.HasBeenDeleted = category_update.HasBeenDeleted

    if duplicates:
        return {"data": f"Loại sản phẩm đã tồn tại: {', '.join(duplicates)}"}

    # Commit the changes to the database
    db.commit()

    return {"data": "Thông tin các loại sản phẩm đã được cập nhật thành công!"}
#Xóa loại sản phẩm
@router.delete("/delete_category/{category_id}", summary="Xóa loại sản phẩm")
async def delete_category(category_id: str, db: Session = Depends(get_database_session)):
    # Check if the category with the given CategoryID exists
    existing_category = db.query(Category).filter(Category.CategoryID == category_id).first()
    if not existing_category:
        raise HTTPException(status_code=404, detail=f"Loại sản phẩm có ID {category_id} không tồn tại!")

    # Soft delete by marking HasBeenDeleted as True
    existing_category.HasBeenDeleted = "Đã xoá"

    # Commit the changes to the database
    db.commit()

    return {"data": "Loại sản phẩm đã được xóa thành công!"}

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

