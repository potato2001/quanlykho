from fastapi import Depends, FastAPI, Request, Form,status,Header,APIRouter, Query
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import exists
import base64
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from datetime import date
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT,decodeJWT,refresh_access_token
import schema
from database import SessionLocal, engine
import model
from model import ProductSchema


router = APIRouter()  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
#Tạo sản phẩm
@router.post("/create_product",dependencies=[Depends(JWTBearer())], summary="Tạo sản phẩm")
async def create_product(
    db: Session = Depends(get_database_session),
    ProductID: str = Form(...),
    ProviderID: str = Form(...),
    ProductName: str = Form(...),
    CategoryID: str = Form(...),
    #ProductCategory: str = Form(...),
    ProductBrand:str = Form(...),
    ProductSerial:str = Form(...),
    ProductDescription:str = Form(...),
    ReorderQuantity: int = Form(...),
    UnitPrice: float = Form(...),
    Status: str = Form(...),
):
    Product_exists = db.query(exists().where(ProductSchema.ProductID == ProductID)).scalar()
    if Product_exists:
        return {"data": "Sản phẩm đã tồn tại!"}
    ProductSchema = ProductSchema(ProductID = ProductID, ProviderID = ProviderID, ProductName = ProductName, CategoryID=CategoryID, ProductBrand=ProductBrand, ProductSerial=ProductSerial, ProductDescription=ProductDescription, ReorderQuantity=ReorderQuantity, UnitPrice=UnitPrice, Status=Status, HasBeenDeleted=0)
    db.add(ProductSchema)
    db.commit()
    db.refresh(ProductSchema)
    return {
        "data:" "Tạo sản phẩm thành công!"
    }

#Sửa thông tin sản phẩm
@router.put("/update_product",dependencies=[Depends(JWTBearer())], summary="Sửa sản phẩm")
async def update_product(
    db: Session = Depends(get_database_session),
    ProductID: str = Form(...),
    ProviderID: str = Form(...),
    ProductName: str = Form(...),
    CategoryID: str = Form(...),
    ProductBrand:str = Form(...),
    ProductSerial:str = Form(...),
    ProductDescription:str = Form(...),
    ReorderQuantity: int = Form(...),
    UnitPrice: float = Form(...),
):
    product_exists = db.query(exists().where(ProductSchema.ProductID == ProductID)).scalar()
    product = db.query(ProductSchema).get(ProductID)
    if product_exists:
        print(product)
        product.ProductName = ProductName
        product.ProviderID = ProviderID
        product.CategoryID = CategoryID
        product.ProductBrand = ProductBrand
        product.ProductSerial = ProductSerial
        product.ProductDescription = ProductDescription
        product.ReorderQuantity = ReorderQuantity
        product.UnitPrice = UnitPrice
        db.commit()
        db.refresh(product)
        return {
            "data": "Thông tin sản phẩm đã được cập nhật!"
        }
    else:
        return JSONResponse(status_code=400, content={"message": "Không có thông tin sản phẩm!"})

#Xóa sản phẩm
@router.delete("/delete_product",dependencies=[Depends(JWTBearer())], summary="Xóa sản phẩm")
async def delete_product(
    db: Session = Depends(get_database_session),
    ProductID: int = Form(...)
):
    Product_exists = db.query(exists().where(ProductSchema.ProductID == ProductID)).scalar()
    if Product_exists:
        Product = db.query(ProductSchema).get(ProductID)
        Product.hasBeenDeleted=1
        # db.delete(product)
        db.commit()
        db.refresh(Product)

        return{
         "data": "Xóa sản phẩm thành công!"
        }
    else:
        return JSONResponse(status_code=400, content={"message": "Không tồn tại sản phẩm!"})

#Lấy sản phẩm theo mã sản phẩm
@router.get("/Product/{ProductID}", summary="Lấy sản phẩm theo mã")
def get_courses_with_subject_info(
    db: Session = Depends(get_database_session),
    ProductID = str
):
    Product = (
    db.query(ProductSchema)  # Specify the model (ProductSchema) to query
    .filter(ProductSchema.ProductID == ProductID)
    .all()
    )
    print(Product)
    result = []
    for product in Product:
        result.append(
            {   
              product
            }
        )
    return {"data": result}

#Lấy tất cả sản phẩm
@router.get("/Product", summary="Lấy tất cả sản phẩm")
def get_products(
    db: Session = Depends(get_database_session),
):
    Product = (
    db.query(ProductSchema)  # Specify the model (ProductSchema) to query
    .all()
    )
    print(Product)
    result = []
    for product in Product:
        result.append(
            {   
              product
            }
        )
    return {"data": result}

#Lấy tất cả sản phẩm còn trong kho
@router.get("/Product/All", summary="Lấy sản phẩm theo mã")
def get_all_products(
    db: Session = Depends(get_database_session),
):
    Product = (
    db.query(ProductSchema) 
    .filter(ProductSchema.ReorderQuantity>0,ProductSchema.HasBeenDeleted == 0)
    .all()
    )
    print(Product)
    result = []
    for Product in Product:
        result.append(
            {   
              Product
            }
        )
    return {"data": result}

#Lấy tất cả sản phẩm theo hãng
@router.get("/Product/All/ProductBrand", summary="Lấy sản phẩm theo hãng")
def get_all_products_with_brand(
    ProductBrand: str = Query(None),
    db: Session = Depends(get_database_session),
):
    query = (
        db.query(ProductSchema)
    )

    if ProductBrand:
        query = query.filter(ProductSchema.ProductBrand == ProductBrand)

    Product = query.all()
    result = []
    for Product in Product:
        result.append(
            {   
              Product
            }
        )
    return {"data": result}

#Lấy tất cả sản phẩm theo hãng và còn hàng (chạy không lọc ra theo hãng)
@router.get("/Product/All/ProductBrand/Instock", summary="Lấy sản phẩm theo hãng và còn hàng")
def get_all_products_with_brand_instock(
    ProductBrand: str = Query(None),
    db: Session = Depends(get_database_session),
):
    query = (
        db.query(ProductSchema)
        .filter(ProductSchema.ReorderQuantity > 0, ProductSchema.HasBeenDeleted == 0)
    )

    if ProductBrand:
        query = query.filter(ProductSchema.ProductBrand == ProductBrand)

    Product = query.all()
    result = []
    for Product in Product:
        result.append(
            {   
              Product
            }
        )
    return {"data": result}

#Lấy tất cả sản phẩm theo loại
@router.get("/Product/All/Category", summary="Lấy sản phẩm theo loại")
def get_all_products_with_category(
    CategoryID: str = Query(None),
    db: Session = Depends(get_database_session),
):
    query = (
        db.query(ProductSchema)
    )

    if CategoryID:
        query = query.filter(ProductSchema.CategoryID == CategoryID)

    Product = query.all()
    result = []
    for Product in Product:
        result.append(
            {   
              Product
            }
        )
    return {"data": result}

#Lấy tất cả sản phẩm thuộc loại được chọn và còn hàng
@router.get("/Product/All/ProductCategory/Instock", summary="Lấy sản phẩm theo loại và còn hàng")
def get_all_products_with_category(
    CategoryID: str = Query(None),
    db: Session = Depends(get_database_session),
):
    query = (
        db.query(ProductSchema)
        .filter(ProductSchema.ReorderQuantity > 0, ProductSchema.HasBeenDeleted == 0)
    )
#dadad
    if CategoryID:
        query = query.filter(ProductSchema.CategoryID == CategoryID)

    Product = query.all()
    result = []
    for Product in Product:
        result.append(
            {   
              Product
            }
        )
    return {"data": result}
