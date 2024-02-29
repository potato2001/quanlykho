from typing import Text
from sqlalchemy import Column,Date,BLOB,ForeignKey
from sqlalchemy.types import String, Integer, Text, Float,Double

from database import Base
from sqlalchemy.orm import  relationship


#Sản phẩm
class ProductSchema(Base):
    __tablename__= "Product"
    #ID = Column(Integer, primary_key=True, index=True)
    ProductID = Column(String)
    ProductCode = Column(String)
    SupplierID = Column(String)
    ProductName = Column(String(100))
    ProductCategory = Column(String(45))
    ProductBrand = Column(String(10))
    ProductSerial = Column(String(10), unique=True)
    ProductDescription = Column(String)
    ReorderQuantity = Column(Integer)
    UnitPrice = Column(Integer)
    Status=Column(String)
    HasBeenDeleted=Column(String)


#Nhà cung cấp
class ProviderSchema(Base):
    __tablename__= "Provider"
    ProviderID = Column(Integer, primary_key=True, index=True)
    ProviderName = Column(String(45))
    ProviderAddress = Column(Integer)
    ProviderPhone = Column(String(100),unique=True)
    ProviderEmail = Column(String)
    HasBeenDeleted = Column(String)

#Kho hàng
class InventorySchema(Base):
    __tablename__ = "Inventory"
    InventoryID = Column(Integer, primary_key=True, index=True)
    ProductID = Column(String)
    QuantityAvailable = Column(String)

#Lịch sử kho hàng
class InventoryHistorySchema(Base):
    __tablename__ = "InventoryHistory"
    HistoryID = Column(Integer, primary_key=True, index=True)
    ProductID = Column(String)
    QuantityChange = Column(Integer)
    ChangeDate = Column(String)


#Đơn hàng
class OrderSchema(Base):
    __tablename__= "Order"
    OrderID = Column(Integer, primary_key=True, index=True)
    ProductID = Column(String)
    ProductQuantity=Column(Integer)
    OrderDate = Column(String)
    Status = Column(String)

#Chi tiết đơn hàng
class OrderDetailSchema(Base):
    __tablename__= "OrderDetail"
    OrderDetailID = Column(Integer, primary_key=True, index=True)
    OrderID = Column(Integer)
    ProductID = Column(String)
    OrderQuantity = Column(Integer)
    UnitPrice = Column(String)

#Người dùng
class UserSchema(Base):
    __tablename__= "User"
    UserID = Column(Integer, primary_key=True, index=True)
    UserName = Column(String(45), unique=True)
    UserPassword = Column(String(45), unique=True)
    Role = Column(Integer)

#Phân loại hàng
class CategorySchema(Base):
    __tablename__= "Category"
    CategoryID = Column(Integer,primary_key=True, index=True)
    CategoryName = Column(String)
    HasBeenDeleted=Column(String)

#Hoá đơn
class InvoiceSchema(Base):
    __tablename__ = "Invoice"
    InvoiceID = Column(Integer, primary_key=True, index=True)
    UserID = Column(String)
    OrderDetailID = Column(String)
    TotalCost = (String)