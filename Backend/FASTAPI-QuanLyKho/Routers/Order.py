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
from model import OrderSchema,ProductSchema


router = APIRouter()  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Tạo đơn hàng (Chưa xong và chưa có phần nối với thông tin người đặt)
@router.post("/create_order", summary="Tạo đơn hàng")
async def create_order(
    db: Session = Depends(get_database_session),
    ProductID: str = Form(...),
    ProductQuantity: str = Form(...),
    OrderDate:str=Form(...),
    Status:str=Form(...),
):
    Product = db.query(ProductSchema).filter_by(ProductID=ProductID).first()
    if(Product.ReorderQuantity==0):
        Product.status == 0
        db.commit()
        return JSONResponse(status_code=400, content={"message": "Sản phẩm đã hết"})
    if(ProductQuantity<Product.ReorderQuantity):
        return JSONResponse(status_code=400, content={"message": f"Sản phẩm tồn kho còn {Product.ReorderQuantity}"})
    OrderSchema = OrderSchema(ProductID = ProductID, OrderDate = datetime.today().strftime("%H:%M ,%d-%m-%Y"), Status=0, ProductQuantity=ProductQuantity)
    product.quantity -= quantityProduct
    db.add(ordersSchema)
    db.commit()
    db.refresh(ordersSchema)
    return {
        "data:" "Tạo đơn hàng thành công!"
    }

#Sửa thông tin đơn hàng
@router.put("/update_order",dependencies=[Depends(JWTBearer())], summary="Sửa đơn hàng")
async def update_order(
    db: Session = Depends(get_database_session),
    productId: str = Form(...),
    customerName: str = Form(...),
    phoneNumber:str=Form(...),
    address:str=Form(...),
    quantityProduct:int=Form(...)
):
    order_exists = db.query(exists().where(OrdersSchema.productId == productId)).scalar()
    order = db.query(OrdersSchema).get(productId)
    if order_exists:
        print(order)
        order.productId = productId
        order.customerName = customerName
        order.phoneNumber = phoneNumber
        order.address = address
        order.quantityProduct = quantityProduct
        db.commit()
        db.refresh(order)
        return {
            "data": "Thông tin đơn hàng đã được cập nhật!"
        }
    else:
        return JSONResponse(status_code=400, content={"message": "Không có thông tin đơn hàng!"})

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
