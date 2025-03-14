# Blog API

A REST API for a blog system with user activity logging. The project uses two databases: one for storing blog data (authors_db) and another for storing user activity logs (tech_info_db).

## Project Structure

### Database authors_db
- **users** - System users
  - id (PK)
  - email (unique)
  - login (unique)

- **blog** - User blogs
  - id (PK)
  - owner_id (FK -> users.id)
  - name
  - description

- **post** - Blog posts
  - id (PK)
  - header
  - text
  - author_id (FK -> users.id)
  - blog_id (FK -> blog.id)

### Database tech_info_db
- **space_type** - Action space types
  - id (PK)
  - name (unique) ['global', 'blog', 'post']

- **event_type** - Event types
  - id (PK)
  - name (unique) ['login', 'comment', 'create_post', 'delete_post', 'logout']

- **logs** - User activity logs
  - id (PK)
  - datetime
  - user_id
  - space_type_id (FK -> space_type.id)
  - event_type_id (FK -> event_type.id)

## API Endpoints

### GET /api/comments
Retrieve information about user comments.

**Query Parameters:**
- login (string) - user login

**Response Example:**
```json
[
    {
        "login": "user1",
        "header": "Hello World",
        "author_login": "user2",
        "comment_count": 2
    }
]
```

### GET /api/general
Retrieve general information about user activities.

**Query Parameters:**
- login (string) - user login

**Response Example:**
```json
{
    "date": "2024-03-14",
    "login_count": 1,
    "logout_count": 0,
    "blog_actions_count": 0
}
```

## Getting Started

### Local Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with database connection settings:
```env
AUTHORS_DB_URL=postgresql://postgres:password@localhost:5432/authors_db
TECH_INFO_DB_URL=postgresql://postgres:password@localhost:5432/tech_info_db
```

4. Start the server:
```bash
uvicorn src.main:app --reload
```

### Docker Setup

1. Start the containers:
```bash
docker-compose up --build
```

2. To stop:
```bash
docker-compose down
```

3. To clean all data:
```bash
docker-compose down -v
```

## API Access

After startup, the API will be available at: http://localhost:8000

- Swagger UI (OpenAPI): http://localhost:8000/docs
- API endpoints:
  - http://localhost:8000/api/comments?login=user1
  - http://localhost:8000/api/general?login=user1

## Test Data

The database comes with pre-configured test users:
- user1 (email: user1@example.com)
- user2 (email: user2@example.com)

## Dependencies

- FastAPI
- SQLAlchemy
- Pydantic
- Pydantic-settings
- PostgreSQL
- Uvicorn

## Notes

- The project uses PostgreSQL as the database management system
- All necessary tables and test data are created automatically on first launch
- In Docker version, data is persisted in a named volume postgres_data


