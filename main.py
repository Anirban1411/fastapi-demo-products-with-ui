from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models 
import db_models
from database import SessionLocal, engine, Base

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- CORS Middleware ---
# This allows the frontend (running on localhost:3000)
# to communicate with the backend (running on localhost:8000)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],
)

# --- Dependency Injection for Database Session ---

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API Endpoints ---

@app.get("/")
def greet():
    return {"message":"welcome to the home page"}

@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

# GET a single product by ID
@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product is None:
        return {"error": "Product not found"}
    return db_product

# POST (Create) a new product
@app.post("/products")
def add_product(product: models.Product, db: Session = Depends(get_db)):
    # Convert Pydantic model to SQLAlchemy model
    db_product = db_models.Product(**product.model_dump())
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # Refresh to get the new ID
    return db_product

# PUT (Update) an existing product
@app.put("/products/{id}")
def update_product(id: int, product: models.Product, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    
    if db_product is None:
        return {"error": "Product not found"}
        
    # Update the fields
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    
    db.commit()
    return {"message": "Product updated successfully"}

# DELETE a product
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    
    if db_product is None:
        return {"error": "Product not found"}
        
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}