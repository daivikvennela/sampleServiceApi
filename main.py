from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from database import get_database_connection
from typing import Optional


app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    dob: str
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    dob: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users")
async def create_user(user: User):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email,dob) VALUES (%s, %s, %s)"
    
    values = (user.name, user.email, user.dob)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "User created successfully"}


@app.get("/users")
async def read_users():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    connection.close()
    return users

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    connection.commit()
    connection.close()
    return {"message": f"User with id {user_id} deleted successfully"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate):
    connection = get_database_connection()
    cursor = connection.cursor()
    
    # Build the update query dynamically based on provided fields
    update_fields = []
    values = []
    for field, value in user.dict(exclude_unset=True).items():
        if value is not None:
            update_fields.append(f"{field} = %s")
            values.append(value)
    print("after loop: ", update_fields, values )
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    query = f"UPDATE users SET {', '.join(update_fields)} WHERE id = %s"
    print(query)
    values.append(user_id)
    
    cursor.execute(query, tuple(values))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    
    connection.commit()
    connection.close()
    return {"message": f"User with id {user_id} updated successfully"}
