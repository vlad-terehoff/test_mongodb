from pydantic import Field

from base.user.schemas.address_schemas import AddressDTO, WorkDTO
from src.base.base_models.dto_models import BaseDto, PyObjectId


class UserDTO(BaseDto):
    loggin: str | None = Field(max_length=256, default=None)
    first_name: str | None = Field(max_length=256, default=None)
    last_name: str | None = Field(max_length=256, default=None)
    age: int | None = Field(default=None)
    address: AddressDTO
    work: WorkDTO | None = Field(default=None)


class UserGet(BaseDto):
    loggin: str | None = Field(max_length=256, default=None)
    first_name: str | None = Field(max_length=256, default=None)
    last_name: str | None = Field(max_length=256, default=None)


# class GetUserDTO(BaseDto):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     loggin: str | None = Field(max_length=256, default=None)
#     first_name: str | None = Field(max_length=256, default=None)
#     last_name: str | None = Field(max_length=256, default=None)
#     age: int | None = Field(default=None)
#     city: str | None = Field(default=None)

class GetUserDTO(BaseDto):
    id: PyObjectId = Field(alias="_id")
    loggin: str | None = Field(max_length=256, default=None)
    first_name: str | None = Field(max_length=256, default=None)
    last_name: str | None = Field(max_length=256, default=None)
    age: int | None = Field(default=None)
    address: AddressDTO
    work: WorkDTO | None = Field(default=None)

class GetUserSHDTO(BaseDto):
    id: str = Field(alias="_id")
    loggin: str | None = Field(max_length=256, default=None)
    first_name: str | None = Field(max_length=256, default=None)
    last_name: str | None = Field(max_length=256, default=None)
    age: int | None = Field(default=None)
    address: AddressDTO
    work: WorkDTO | None = Field(default=None)