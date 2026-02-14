from fastapi import FastAPI
import routers
from database import Base, engine
import models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Minimal Ecommerce API")
app.include_router(routers.auth_router, prefix="/auth", tags=["Auth"])
app.include_router(routers.product_router, prefix="/products", tags=["Products"])
app.include_router(routers.blog_router, prefix="/blogs", tags=["Blogs"])
app.include_router(routers.comment_router, prefix="/comments", tags=["Comments"])