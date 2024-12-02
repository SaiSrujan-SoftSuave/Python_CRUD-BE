from uuid import UUID

from fastapi import FastAPI, HTTPException

from app.userModels.user import User, UserUpdateRequest
from repository.userDb import userDb

app = FastAPI()


@app.get("/")
def root():
    return {"hello": "hello"}


@app.get("/api/v1/users")
def fetch_users():
    return userDb


@app.post("/api/v1/users")
def add_user(user: User):
    userDb.append(user)
    return user.id


@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id: UUID):
    for user in userDb:
        if user.id == user_id:
            userDb.remove(user)
            return {
                "message": "user successfully removed 🚀",
                "user": user
            }
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.put("/api/v1/users/{user_id}")
def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in userDb:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.first_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {
                "message": "user successfully updated 🚀",
                "user": user
            }
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist to update"
    )
