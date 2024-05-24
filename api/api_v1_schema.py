from typing import List

from django.contrib.auth.models import User
from ninja import ModelSchema
from ninja import Schema


class UserSchema(ModelSchema):
    class Meta:
        model = User
        exclude = ["password"]


class ErrorOut(Schema):
    message: str


class CarIn(Schema):
    name: str
    type: str
    color: str
    capacity: int
    capacity_unit: str


class CarOut(Schema):
    name: str
    type: str
    color: str
    capacity: int
    capacity_unit: str


class CarGarageOut(Schema):
    car: CarOut
    parked_at: str
    position: str = None


class GarageOut(Schema):
    name: str
    location: str
    capacity: int
    cars: List[CarOut]
