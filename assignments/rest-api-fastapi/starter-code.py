"""
REST API with FastAPI - Starter Code

This starter code provides a basic FastAPI application structure.
Your task is to implement the todo list API endpoints.

To run this application:
1. Install FastAPI and uvicorn: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Visit http://localhost:8000/docs to see the API documentation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Todo List API", version="1.0.0")

# TODO: Define your Pydantic models here
# Example:
# class Todo(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     completed: bool = False


# In-memory storage for todos (replace with database in production)
todos = []


@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Todo List API! Visit /docs for documentation."}


# TODO: Implement your API endpoints here
# GET /todos - Get all todos
# GET /todos/{todo_id} - Get a specific todo
# POST /todos - Create a new todo
# PUT /todos/{todo_id} - Update a todo
# DELETE /todos/{todo_id} - Delete a todo
