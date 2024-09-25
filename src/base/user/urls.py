from typing import List

from fastapi import APIRouter

from base.user.schemas.address_schemas import GetPermissionDTO, PermissionDTO, GetPermissionShDTO
from base.user.schemas.user_schemas import UserDTO, GetUserDTO, GetUserSHDTO
from src.base.user.models import User, Permission



user_router = APIRouter(prefix="/user", tags=["USER"])


@user_router.post("/add_user", response_model=GetUserSHDTO)
async def add_user_to_db(user: UserDTO):
    user = await User.insert_one({**user.model_dump()})
    return GetUserDTO.model_validate(user).model_dump()

@user_router.get("/get_user/{id}", response_model=GetUserSHDTO)
async def get_user(id):
    user = await User.find_one({'_id': id})
    return GetUserDTO.model_validate(user).model_dump()


@user_router.put("/{id}", response_model=GetUserSHDTO)
async def add_address_to_user(id: str, user: UserDTO):
    user = await User.update_one(query={"_id": id}, update_fields={**user.model_dump()})
    return GetUserDTO.model_validate(user).model_dump()


@user_router.post("/add_permission", response_model=GetPermissionShDTO)
async def add_user_to_db(permission: PermissionDTO):
    permission = await Permission.insert_one({**permission.model_dump()})
    return GetPermissionDTO.model_validate(permission).model_dump()


@user_router.get("/get_all_permission", response_model=List[GetPermissionShDTO])
async def add_user_to_db():
    permissions = await Permission.find_many({})
    return [GetPermissionDTO.model_validate(permission).model_dump() for permission in permissions]


@user_router.post("/add_permission_to_user{id}")
async def add_user_to_db(id_perm: str, id_user: str):
    permission = await Permission.find_one({"_id": id_perm})
    user = await User.find_one({"_id": id_user})

    permission.user = user
    await permission.save()


@user_router.get("/get_permission_user{id}")
async def add_user_to_db(id_user: str):
    user = await User.find_one({"_id": id_user})

    permissions = await Permission.find_many({"user": user._id})

    return [permission.to_dict() for permission in permissions]