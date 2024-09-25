from pydantic import Field
from src.base.base_models.dto_models import BaseDto, PyObjectId


class AddressDTO(BaseDto):
    street: str | None = Field(max_length=256, default=None)
    city: str | None = Field(max_length=256, default=None)


class WorkDTO(BaseDto):
    position: str | None = Field(max_length=256, default=None)
    organization: str | None = Field(max_length=256, default=None)


class PermissionDTO(BaseDto):
    name: str


class GetPermissionDTO(BaseDto):
    id: PyObjectId = Field(alias="_id")
    name: str


class GetPermissionShDTO(BaseDto):
    id: str = Field(alias="_id")
    name: str