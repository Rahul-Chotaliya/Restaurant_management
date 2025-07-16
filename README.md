🍽️ Restaurant Management System
  A RESTful API built with Django REST Framework to manage multiple restaurants, their menus, individual dishes, and like features for both restaurants and dishes.
________________________________________
🚀 Features
  •	Manage multiple restaurants (CRUD operations)
  •	Create and manage menus for restaurants
  •	Add dishes to menus
  •	Like/unlike functionality for:
  o	Restaurants
  o	Dishes
  •	Like count tracking for both restaurants and dishes
  •	Token-based authentication for secure access
  •	Admin panel support for data management
________________________________________
📦 Technologies Used
  •	Python 3.x
  •	Django
  •	Django REST Framework
  •	SQLite / PostgreSQL (choose your DB)
  •	djoser / Simple JWT (for auth if used)
  •	drf-yasg (for Swagger documentation, if used)
________________________________________
🔧 Installation
  1.	Clone the repository:
    bash
    CopyEdit
    git clone [https://github.com/yourusername/restaurant-management-system.git](https://github.com/Rahul-Chotaliya/Restaurant_management.git)
    cd restaurant-management-system
  2.	Create a virtual environment:
    bash
    CopyEdit
    python -m venv env
    source env/bin/activate   # on Windows: env\Scripts\activate
  3.	Install dependencies:
    bash
    CopyEdit
    pip install -r requirements.txt
  4.	Apply migrations:
    bash
    CopyEdit
    python manage.py migrate
  5.	Create a superuser:
    bash
    CopyEdit
    python manage.py createsuperuser
  6.	Run the development server:
    bash
    CopyEdit
    python manage.py runserver
________________________________________
🔐 API Authentication
  This project uses token-based authentication.
  •	Login to get a token:
  http
  CopyEdit
  POST /api/token/
  •	Use the token in headers:
  makefile
  CopyEdit
  Authorization: Bearer <your_token>
________________________________________
📂 Project Structure
  bash
  CopyEdit
  restaurant-management-system/
  ├── manage.py
  ├── restaurant/           # App for managing restaurants, menus, dishes
  │   ├── models.py
  │   ├── views.py
  │   ├── serializers.py
  │   ├── urls.py
  │   └── ...
  ├── users/                # App for user authentication (optional)
  ├── core/                 # Settings and base config
  ├── requirements.txt
  └── README.md
________________________________________
🔄 API Endpoints (Examples)
  Method	Endpoint	Description
  GET	/api/restaurants/	List all restaurants
  POST	/api/restaurants/	Create a new restaurant
  GET	/api/menus/?restaurant=1	List menu of restaurant 1
  POST	/api/likes/restaurant/1/	Like restaurant with ID 1
  POST	/api/likes/dish/5/	Like dish with ID 5
