# 🚀 FastAPI Production Backend

![Banner](./banner.png)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-Migrations-blue?style=for-the-badge)](https://alembic.sqlalchemy.org/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge&logo=json-web-tokens)](https://jwt.io/)

A professional, enterprise-grade FastAPI backend template designed for scalability, security, and developer productivity. This project implements a modern asynchronous architecture with a modular structure, making it perfect for production-ready applications.

## ✨ Key Features

- **🔐 Robust Authentication**: Fully implemented JWT-based auth system including user registration, login, and secure "me" endpoints.
- **🏗️ Modular Architecture**: Organized by features/modules (`auth`, `blog`) for high maintainability and scalability.
- **⚡ Asynchronous Performance**: Built from the ground up to leverage Python's `asyncio` for high-concurrency workloads.
- **🗄️ Advanced ORM**: Utilizes SQLAlchemy 2.0 with asynchronous drivers (`aiosqlite`) for efficient database operations.
- **🔄 Database Migrations**: Seamless schema management using Alembic.
- **🛠️ Production Ready**: Includes structured configuration, dependency injection, and clean separation of concerns.
- **📖 Auto-Generated Docs**: Interactive API documentation via Swagger UI and ReDoc.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: [Python 3.11+](https://www.python.org/)
- **Database ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Security**: [Jose (JWT)](https://python-jose.readthedocs.io/), [Passlib (Argon2)](https://passlib.readthedocs.io/)
- **Environment Management**: `.env` with `python-dotenv`

## 🚀 Getting Started

   git clone https://github.com/huzaifakhter/jksuperapp_backend.git
   cd fastapi-production-backend
   ```

2. **Set up virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   uv pip install -r pyproject.toml
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory (refer to `.env.example` if available):
   ```env
   DATABASE_URL="sqlite+aiosqlite:///./dev.db"
   SECRET_KEY="your-super-secret-key"
   ALGORITHM="HS256"
   ACCESS_TOKEN_MINUTES=30
   ```

### Database Migrations

This project uses Alembic for database migrations. To apply migrations or create new ones:

```bash
# Apply pending migrations
alembic upgrade head

# Create a new migration
alembic revision --autogenerate -m "description of changes"
```

### Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## 📂 Project Structure

```text
├── alembic/              # Database migration scripts
├── app/
│   ├── core/             # Core configurations (DB, Security, Dependencies)
│   ├── infrastructure/   # External service integrations
│   ├── modules/          # Feature-based modules
│   │   ├── auth/         # Authentication & User Management
│   │   └── blog/         # Blog/Content Management
│   └── main.py           # Application entry point
├── pyproject.toml        # Project dependencies and metadata
└── README.md             # You are here!
```

## 📜 API Endpoints

### Authentication
- `POST /auth/register` - Create a new user account
- `POST /auth/login` - Authenticate and receive JWT token
- `GET /auth/me` - Get current authenticated user details
- `GET /auth/users` - List all registered users (Admin only)

### Blog
- `GET /blog/blog` - Retrieve blog posts (Requires Auth)

## 📡 Documentation

Once the server is running, you can access the interactive documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Built with ❤️ by [Antigravity](https://github.com/huzaifakhter)
