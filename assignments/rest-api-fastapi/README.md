# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a RESTful API using the FastAPI framework, including creating endpoints, handling HTTP methods, and working with request/response models.

## 📝 Tasks

### 🛠️ Create a Todo List API

#### Description
Build a REST API for managing a todo list with endpoints to create, read, update, and delete todo items.

#### Requirements
Completed program should:

- Define a Todo model with fields: id, title, description, and completed status
- Create a GET endpoint to retrieve all todos
- Create a GET endpoint to retrieve a single todo by ID
- Create a POST endpoint to add a new todo
- Create a PUT endpoint to update an existing todo
- Create a DELETE endpoint to remove a todo
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Use FastAPI's automatic API documentation at /docs


### 🛠️ Add Data Validation

#### Description
Implement request validation using Pydantic models to ensure data integrity.

#### Requirements
Completed program should:

- Use Pydantic models for request and response validation
- Validate that title is required and not empty
- Validate that completed is a boolean value
- Return clear error messages for invalid input (422 status)
- Include example values in the API documentation
