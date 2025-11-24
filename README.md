FastAPI Products API (PostgreSQL)

A simple and clean FastAPI + PostgreSQL backend project demonstrating basic CRUD operations for products.
You can interact with the API using FastAPI Docs (/docs) or Postman.

Tech Stack

Backend: FastAPI
Database: PostgreSQL
ORM / Driver: SQLAlchemy 
API Testing: Swagger UI (FastAPI Docs), Postman
Environment: Python Virtual Environment
Version Control: Git & GitHub


🔍 Features

Create new products
Get all products
Get a single product by ID
Update product details
Delete a product
PostgreSQL database integration
Auto-generated documentation via Swagger UI

📂 Project Structure
fastapi-demo-products-with-ui/
│
├── main.py            # Entry point for FastAPI
├── models.py          # Product models / DB logic
├── requirements.txt   # Python dependencies
└── venv/ (optional)   # Your virtual environment (not pushed to GitHub)

🛠️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/Anirban1411/fastapi-demo-products-with-ui.git
cd fastapi-demo-products-with-ui

2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac / Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure PostgreSQL
Create a database:

CREATE DATABASE products_db;

Update your database connection string inside your project if needed:
postgresql://username:password@localhost:5432/products_db

Replace:
username
password

5️⃣ Run the FastAPI Server
uvicorn main:app --reload

▶️ API Usage
After the server starts, open:

FastAPI Docs (Swagger UI)
http://127.0.0.1:8000/docs


You can test all endpoints directly here.

API Endpoints Overview
Method	Endpoint	Description
GET	/products	Get all products
GET	/products/{id}	Get product by ID
POST	/products	Create new product
PUT	/products/{id}	Update product details
DELETE	/products/{id}	Delete product

(Adjust if your code uses different paths.)


Author

Anirban Biswas
GitHub: @Anirban1411


