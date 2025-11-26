from pydantic import BaseModel, Field
from typing import Optional


class CattItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0,
                          description="Quantity (must be greater than 0)")


class CartItemCreate(CattItemBase):
    pass

class CattItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0,
                          description="Quantity (must be greater than 0)")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Product quantity")
    subtotal: float = Field(...,
                            description="Total price for this product (price * quantity)")
    image_url: Optional[str] = Field(None, description="Product image URL")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")