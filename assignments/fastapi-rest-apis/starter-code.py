from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define the Todo data model
class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    description: str = ""
    completed: bool = False

# In-memory storage for todos (replace with database in Task 2)
todos_db: List[Todo] = []
next_id = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

# TODO: Implement the following endpoints:
# 1. GET /todos - retrieve all todos
# 2. GET /todos/{todo_id} - retrieve a specific todo
# 3. POST /todos - create a new todo
# 4. PUT /todos/{todo_id} - update a todo
# 5. DELETE /todos/{todo_id} - delete a todo

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)