# 🛍️ E-commerce API

This repository contains an **e-commerce API** built using Django and Django Rest Framework (DRF). The API provides functionalities for managing products, categories, orders, and authentication. It is designed to be **flexible**, **scalable**, and **easy to use**.

## ✨ Features

- 🛒 **Product Management**: Add, view, update, and delete products.
- 📂 **Category Management**: View a list of product categories.
- 📦 **Order Management**: Create and manage customer orders.
- 🔍 **Filtering & Search**: Search products by name and filter by price, stock, etc.
- 🔑 **Authentication**: JWT-based authentication.
- 📜 **API Documentation**: Auto-generated Swagger and Redoc documentation.

## 🌐 Endpoints

### 🆓 Public Endpoints
- **`/products/`**: View and create products (Admins only for creation).
- **`/products/id/<product_id>/`**: View, update, or delete a specific product (Admins only for update and delete).
- **`/products/info/`**: Get aggregate product information (e.g., count, max price).
- **`/category/`**: View a list of categories.

### 🔒 Authenticated Endpoints
- **`/orders/`**: Create and manage orders (only accessible by authenticated users).
- **`/api/token/`**: Obtain JWT token.
- **`/api/token/refresh/`**: Refresh JWT token.

### 🏠 API Root
- **`/`**: Provides a list of available endpoints with sample links for navigation.

### 📖 API Documentation
- **`/api/schema/`**: OpenAPI schema.
- **`/api/schema/swagger-ui/`**: Swagger UI documentation.
- **`/api/schema/redoc/`**: Redoc documentation.

## 🚀 Installation

### Prerequisites
- 🐍 Python 3.8+
- 🌐 Django 4.0+
- 🛠️ Django Rest Framework
- 🐘 PostgreSQL (or any preferred database)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>


🛠️ Usage

🔑 Authentication
Use the /api/token/ endpoint to obtain a JWT token.
Include the token in the Authorization header as:
makefile
Copy code
Authorization: Bearer <token>
📖 Pagination
The product list supports pagination with customizable page sizes:
Use the size query parameter to specify the number of items per page.
Maximum page size is 1000.
🔍 Filtering and Searching
Search products by name using the search query parameter.
Filter products by price, stock, or category.
📂 Project Structure
products/: Contains the core functionality for managing products, categories, and orders.
products/views.py: API views for handling business logic.
products/serializers.py: Serializers for transforming data between models and API responses.
products/models.py: Database models for the application.
products/urls.py: Application-specific URLs.
filter.py: Custom filters for querying products and orders.
📜 API Documentation
This project uses drf-spectacular to generate OpenAPI documentation.

📄 Swagger UI: /api/schema/swagger-ui/
📄 Redoc: /api/schema/redoc/