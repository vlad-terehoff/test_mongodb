from fastapi import FastAPI
from motormongo import DataBase, get_db
from base.user.urls import user_router
from src.base.settings import settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await DataBase.connect(uri=settings.database_url, db=settings.db_name)
    db = await get_db()
    collection = db["user"]
    result = await collection.create_index(
        [("loggin", 1), ("first_name", 1)],  # 1 для индекса по возрастанию
        unique=True
    )
    yield
    await DataBase.close()


app = FastAPI(lifespan=lifespan)


app.include_router(user_router)

# @app.post("/add_user")
# async def add_user_to_db(user: UserDTO, session=Depends(db_helper.get_session)):
#
#     async with session as client:
#         collection = client["user"]
#         await collection.insert_one(user.model_dump(exclude_none=True))
#
#     return {"message": "ok"}


# @app.get("/get_user/{loggin}")
# async def get_user(loggin, session=Depends(db_helper.get_session)):
#
#     async with session as client:
#         collection = client["user"]
#         # cursor = collection.find({"_id": PyObjectId(id)})
#         #
#         # users = cursor.to_list(length=None)
#
#         # cursor = collection.find({"_id": PyObjectId(id)})
#         cursor = collection.find({"loggin": loggin})
#         users = [GetUserDTO.model_validate(user) async for user in cursor]
#
#     return users

