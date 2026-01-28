# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, fast REST APIs using the FastAPI framework. You'll create a complete API with multiple endpoints, request validation, and error handling to understand the fundamentals of building scalable web services.

## 📝 Tasks

### 🛠️ Create a Todo API

#### Description
Build a REST API for managing a todo list using FastAPI. Implement endpoints for creating, reading, updating, and deleting todos, with proper data validation and error responses.

#### Requirements
Completed program should:

- Define a Todo data model with title, description, and completion status fields
- Implement GET endpoint to retrieve all todos or a specific todo by ID
- Implement POST endpoint to create a new todo with validation
- Implement PUT endpoint to update an existing todo
- Implement DELETE endpoint to remove a todo
- Return appropriate HTTP status codes and error messages

### 🛠️ Add Database Persistence

#### Description
Extend your API to persist todos using a database. Implement storage and retrieval of todos so data is maintained between requests.

#### Requirements
Completed program should:

- Use a database (SQLite or similar) to store todo data
- Connect FastAPI to the database using an ORM (e.g., SQLAlchemy)
- Ensure todos are retrieved from and saved to the database
- Handle database errors gracefully with appropriate responses
- Test that todos persist after server restart