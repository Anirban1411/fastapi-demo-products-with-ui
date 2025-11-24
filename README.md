FastAPI Products API (PostgreSQL)

A simple and clean FastAPI backend project built with PostgreSQL.
It demonstrates basic CRUD operations for managing products.
The API can be tested using FastAPI's built-in documentation (/docs) or Postman.

Tech Stack

FastAPI

PostgreSQL

SQLAlchemy

Python Virtual Environment

Git & GitHub

Features

Create new products

Retrieve all products

Retrieve a product by ID

Update product details

Delete a product

Integrated with PostgreSQL

Auto-generated API documentation using FastAPI Docs

Project Structure
fastapi-demo-products-with-ui/
│
├── main.py              # FastAPI application
├── models.py            # Database models and SQLAlchemy logic
├── requirements.txt     # Project dependencies
└── venv/ (optional)     # Virtual environment (not included in Git)

Setup and Installation
1. Clone the Repository
git clone https://github.com/Anirban1411/fastapi-demo-products-with-ui.git
cd fastapi-demo-products-with-ui

2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate     # For macOS and Linux

3. Install Dependencies
pip install -r requirements.txt

4. Configure PostgreSQL

Create the database:

CREATE DATABASE products_db;


Update your database connection string inside the project if necessary:

postgresql://username:password@localhost:5432/products_db


Replace username and password with your PostgreSQL credentials.

5. Run the FastAPI Server
uvicorn main:app --reload

API Usage

Once the server is running, open the following URL in your browser:

http://127.0.0.1:8000/docs


This provides an interactive interface for testing all endpoints.

API Endpoints
Method	Endpoint	Description
GET	/products	Get all products
GET	/products/{id}	Get product by ID
POST	/products	Create a new product
PUT	/products/{id}	Update product
DELETE	/products/{id}	Delete product

(Modify based on your actual routes if needed.)

Author

Anirban Biswas
GitHub: @Anirban1411

