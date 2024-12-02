from typing import List
from uuid import UUID

from app.userModels.user import Gender, Role, User

userDb: List[User] = [
    User(
        id=UUID("7977b7eb-266a-4295-8f7f-6c3f823523ef"),
        first_name="Raju",
        last_name="King",
        gender=Gender.male,
        roles=[Role.user]
    ),
    User(
        id=UUID("2e927a62-a0bd-4dff-aa03-adb1e134ff28"),
        first_name="Anna",
        last_name="Smith",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("dc1920a2-64cd-4f86-97e8-557f859b2e24"),
        first_name="Sam",
        last_name="Brown",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("5c3cf1ac-35f0-4a12-afe4-2f6181ad636b"),
        first_name="Sasha",
        last_name="Lee",
        gender=Gender.female,
        roles=[Role.user, Role.admin]
    ),
]
