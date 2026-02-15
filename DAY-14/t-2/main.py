from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from inventory import Inventory
from models import Electronics, Grocery, Product

app = FastAPI(title="OOP Inventory Management System")

inventory = Inventory()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
class ProductSchema(BaseModel):
    type: str
    name: str
    price: float
    stock: int
    brand: str | None = None
    expiry_date: str | None = None
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/products")
def get_products():
    return inventory.get_all()

@app.post("/add-product")
def add_product(product: ProductSchema):
    try:
        ptype = product.type.lower()

        if ptype == "electronics":
            new_product = Electronics(
                product.name, product.price,
                product.stock, product.brand
            )
        elif ptype == "grocery":
            new_product = Grocery(
                product.name, product.price,
                product.stock, product.expiry_date
            )
        else:
            new_product = Product(
                product.name, product.price,
                product.stock
            )

        inventory.add_product(new_product)
        return {"message": "Product added successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/remove-product/{name}")
def remove_product(name: str):
    try:
        inventory.remove_product(name)
        return {"message": "Product removed"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.put("/update-stock/{name}/{stock}")
def update_stock(name: str, stock: int):
    try:
        inventory.update_stock(name, stock)
        return {"message": "Stock updated"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/search/{name}")
def search_product(name: str):
    product = inventory.search(name)
    if product:
        return product.get_details()
    raise HTTPException(status_code=404, detail="Product not found")
