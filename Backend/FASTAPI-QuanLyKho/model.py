from typing import Text
from sqlalchemy import Column,Date,BLOB,ForeignKey
from sqlalchemy.types import String, Integer, Text, Float

from database import Base
from sqlalchemy.orm import  relationship


#Sản phẩm
class ProductModel(Base):
    __tablename__= "Product"
    ProductID = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String(100))
    ProductBrand = Column(String(10))
    ProductSerial = Column(String(10), unique=True)
    ProductDescription = Column(String)
    UnitPrice = Column(Integer)
    Status=Column(String)
    HasBeenDeleted=Column(String)
    Category_CategoryID=Column(Integer)
    Provider_ProviderID=Column(Integer)


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

# Người dùng
class UserSchema(Base):
    __tablename__= "User"
    UserID = Column(Integer, primary_key=True, index=True)
    UserName = Column(String(45), unique=True)
    UserPassword = Column(String(45), unique=True)
    Role = Column(Integer)

#Phân loại hàng
class CategoryModel(Base):
    __tablename__= "Category"
    CategoryID = Column(Integer,primary_key=True, index=True)
    CategoryName = Column(String)
    HasBeenDeleted=Column(String)

#Hoá đơn
class InvoiceSchema(Base):
    __tablename__ = "Invoice"
    InvoiceID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer)
    OrderDetailID = Column(String)
    TotalCost = (String)

#Khách hàng
class CustomerSchema(Base):
    __tablename__ = "Customer"
    CustomerID = Column(Integer, primary_key=True, index=True)
    CustomerName = Column(String)
    CustomerAddress = Column(String)
    CustomerPhone = Column(String)
    CustomerEmail = Column(String)
