from fastapi import Depends, FastAPI, Request, Form,status,Header,APIRouter, Query
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import exists
import base64
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT,decodeJWT,refresh_access_token
import schema
from database import SessionLocal, engine
import model
from model import OrdersSchema,ProductSchema


router = APIRouter()  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
#Tạo đơn hàng
@router.post("/create_order", summary="Tạo đơn hàng")
async def create_order(
    db: Session = Depends(get_database_session),
    productId: str = Form(...),
    customerName: str = Form(...),
    phoneNumber:str=Form(...),
    address:str=Form(...),
    quantityProduct:int=Form(...)
):
    product = db.query(ProductSchema).filter_by(productId=productId).first()
    if(product.quantity==0):
        product.status == 0
        db.commit()
        return JSONResponse(status_code=400, content={"message": "Sản phẩm đã hết"})
    if(product.quantity<quantityProduct):
        return JSONResponse(status_code=400, content={"message": f"Sản phẩm tồn kho còn {product.quantity}"})
    ordersSchema = OrdersSchema(productId = productId,customerName = customerName, orderDate = datetime.today().strftime("%H:%M ,%d-%m-%Y"),phoneNumber=phoneNumber,address=address,status=0,quantityProduct=quantityProduct)
    product.quantity -= quantityProduct
    db.add(ordersSchema)
    db.commit()
    db.refresh(ordersSchema)
    return {
        "data:" "Tạo đơn hàng thành công!"
    }

# #Sửa thông tin sản phẩm
# @router.put("/update_product",dependencies=[Depends(JWTBearer())], summary="Sửa sản phẩm")
# async def update_product(
#     db: Session = Depends(get_database_session),
#     productId: str = Form(...),
#     supplierId: str = Form(...),
#     productName: str = Form(...),
#     categoryId: str = Form(...),
#     brand:str = Form(...),
#     serial:str = Form(...),
#     description:str = Form(...),
#     quantity: int = Form(...),
#     unitPrice: float = Form(...),
#     hasBeenDeleted:int=Form(...)
# ):
#     product_exists = db.query(exists().where(ProductSchema.productId == productId)).scalar()
#     product = db.query(ProductSchema).get(productId)
#     if product_exists:
#         print(product)
#         product.productName = productName
#         product.supplierId = supplierId
#         product.categoryId = categoryId
#         product.brand = brand
#         product.serial = serial
#         product.description = description
#         product.quantity = quantity
#         product.unitPrice = unitPrice
#         db.commit()
#         db.refresh(product)
#         return {
#             "data": "Thông tin sản phẩm đã được cập nhật!"
#         }
#     else:
#         return JSONResponse(status_code=400, content={"message": "Không có thông tin sản phẩm!"})

# #Xóa sản phẩm
# @router.delete("/delete_product",dependencies=[Depends(JWTBearer())], summary="Xóa sản phẩm")
# async def delete_product(
#     db: Session = Depends(get_database_session),
#     Id: int = Form(...)
# ):
#     product_exists = db.query(exists().where(ProductSchema.Id == Id)).scalar()
#     if product_exists:
#         product = db.query(ProductSchema).get(Id)
#         product.hasBeenDeleted=1
#         # db.delete(product)
#         db.commit()
#         db.refresh(product)

#         return{
#          "data": "Xóa sản phẩm thành công!"
#         }
#     else:
#         return JSONResponse(status_code=400, content={"message": "Không tồn tại sản phẩm!"})

#Lấy đơn hàng
@router.get("/order/{orderId}", summary="Lấy đơn hàng theo mã")
def get_order_by_id(
    db: Session = Depends(get_database_session),
    orderId= int
):
    orders = (
        db.query(
            ProductSchema.productName,
            ProductSchema.serial,
            ProductSchema.unitPrice*OrdersSchema.quantityProduct,
            OrdersSchema
        )
        .join(ProductSchema, ProductSchema.productId == OrdersSchema.productId)
        .filter(OrdersSchema.orderId == orderId)
        .first()
    )

    if not orders:
        return JSONResponse(status_code=404, content={"message": "Không có Order nào!"})

    result = {
        "productName": orders[0],
        "serial": orders[1],
        "price": orders[2],
        "orderInfo":orders[3]
    }

    return {"data": result}

#Lấy tất cả đơn hàng
@router.get("/orders/all", summary="Lấy tất cả đơn hàng")
def get_all_order(
    db: Session = Depends(get_database_session),
):
    orders = (
        db.query(
            ProductSchema.productName,
            ProductSchema.serial,
            ProductSchema.unitPrice*OrdersSchema.quantityProduct,
            OrdersSchema
        )
        .join(ProductSchema, ProductSchema.productId == OrdersSchema.productId)
        .all()
    )

    if not orders:
        return JSONResponse(status_code=404, content={"message": "Không có Order nào!"})

    result = []
    for order in orders:
        result.append(
            {   
            "productName":order[0],
            "serial":order[1],
            "price":order[2],
            "orderInfo":order[3]
            }
        )
    return {"data": result}

#Lấy đơn hàng theo tên khách hàng (chưa xong)
@router.get("/order/{customerName}", summary="Lấy đơn hàng theo tên khách hàng")
def get_order_by_customer_name(
    db: Session = Depends(get_database_session),
    customerName= str
):
    orders = (
        db.query(
            ProductSchema.productName,
            ProductSchema.serial,
            ProductSchema.unitPrice*OrdersSchema.quantityProduct,
            OrdersSchema
        )
        .join(ProductSchema, ProductSchema.productId == OrdersSchema.productId)
        .filter(OrdersSchema.customerName == customerName)
        .first()
    )

    if not orders:
        return JSONResponse(status_code=404, content={"message": "Không có đơn hàng nào của mã khách hàng này!"})

    result = {
        "productName": orders[0],
        "serial": orders[1],
        "price": orders[2],
        "orderInfo":orders[3]
    }


# #Lấy tất cả sản phẩm theo hãng và còn hàng (chạy không lọc ra theo hãng)
# @router.get("/products/all/brand/instock", summary="Lấy sản phẩm theo hãng và còn hàng")
# def get_all_products_with_category(
#     brand: str = Query(None, description="Filter products by brand"),
#     db: Session = Depends(get_database_session),
# ):
#     query = (
#         db.query(ProductSchema)
#         .filter(ProductSchema.quantity > 0, ProductSchema.hasBeenDeleted == 0)
#     )

#     if brand:
#         query = query.filter(ProductSchema.brand == brand)

#     products = query.all()
#     result = []
#     for product in products:
#         result.append(
#             {   
#               product
#             }
#         )
#     return {"data": result}

# #Lấy tất cả sản phẩm theo loại
# @router.get("/products/all/category", summary="Lấy sản phẩm theo loại")
# def get_all_products_with_category(
#     categoryId: str = Query(None, description="Lọc sản phẩm theo loại"),
#     db: Session = Depends(get_database_session),
# ):
#     query = (
#         db.query(ProductSchema)
#     )

#     if categoryId:
#         query = query.filter(ProductSchema.categoryId == categoryId)

#     products = query.all()
#     result = []
#     for product in products:
#         result.append(
#             {   
#               product
#             }
#         )
#     return {"data": result}

# #Lấy tất cả sản phẩm thuộc loại được chọn và còn hàng
# @router.get("/products/all/category/instock", summary="Lấy sản phẩm theo loại và còn hàng")
# def get_all_products_with_category(
#     categoryId: str = Query(None, description="Lọc sản phẩm theo loại và còn hàng"),
#     db: Session = Depends(get_database_session),
# ):
#     query = (
#         db.query(ProductSchema)
#         .filter(ProductSchema.quantity > 0, ProductSchema.hasBeenDeleted == 0)
#     )

#     if categoryId:
#         query = query.filter(ProductSchema.categoryId == categoryId)

#     products = query.all()
#     result = []
#     for product in products:
#         result.append(
#             {   
#               product
#             }
#         )
#     return {"data": result}
