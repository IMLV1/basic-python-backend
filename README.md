
# Basic Python Backend with FastAPI

This project is a simple RESTful API built with **FastAPI**, using **SQLite** as the database, and supporting **JWT Authentication**. It's designed for quick backend development with Python.

## 🔧 Technologies

- **FastAPI** – Web framework for building APIs
- **SQLite** – Lightweight database for development
- **SQLAlchemy** – ORM for database operations
- **Pydantic** – Data validation
- **PyJWT** – JWT token generation and verification
- **Passlib** – Password hashing
- **Uvicorn** – ASGI server

## ⚙️ Installation & Setup

### 1. Clone the project

```bash
git clone https://github.com/IMLV1/basic-python-backend.git
cd basic-python-backend
```

### 2. Create & activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python init_db.py
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

Open your browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see Swagger UI and test the API.

---

## 🔐 JWT Authentication

- **POST** `/auth/login` – Obtain a JWT token using `username` and `password`
- **GET** `/users/me` – Retrieve the current user using the JWT token

---

## 📁 Project Structure

```
basic-python-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py
│       ├── users.py
│       └── auth.py
├── .env.example
├── requirements.txt
├── init_db.py
└── .gitignore
```

---

## 🧪 Testing

Supports **pytest**:

```bash
pytest
```

---

## 🛠️ Development in PyCharm

1. Open the project in PyCharm  
2. Go to `File → Settings → Project: basic-python-backend → Python Interpreter`  
3. Click the gear icon (⚙️) → `Add...`  
4. Choose `New environment` → Name it `.venv`  
5. Select Python 3.13 (or your installed version)  
6. Click `OK` to create the virtual environment  

---

## 📄 Files Not to Commit

- `.env` – Local environment settings  
- `.idea/` – PyCharm IDE settings  
- `*.log` – Log files  

---

## 📄 Recommended `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.sqlite3

# Virtual Environment
.venv/
env/
venv/

# PyCharm
.idea/

# Environment files
.env

# Logs
*.log
```
