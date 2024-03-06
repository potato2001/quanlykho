from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List


class ProductSchema(BaseModel):
    ProductID :str
    ProductName :str
    ProductCategory :str
    ProductBrand :str
    ProductSerial :str
    ProductDescription: Optional[str] = None  
    UnitPrice :int
    Status:str
    HasBeenDeleted:str
    Category_CategoryID:int
    Provider_ProviderID:int
class CategorySchema(BaseModel):
    CategoryName :Optional[str] = None  
    HasBeenDeleted:Optional[str] = None 
class CategoryUpdateSchema(BaseModel):
    CategoryID: int
    CategoryName: str
    HasBeenDeleted: str

class MultipleCategoriesSchema(BaseModel):
    categories: List[CategorySchema]