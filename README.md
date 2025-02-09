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





