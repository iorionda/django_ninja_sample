from typing import List

from ninja import NinjaAPI

from api.api_v1_schema import CarIn
from api.api_v1_schema import CarOut
from api.api_v1_schema import ErrorOut
from api.api_v1_schema import GarageOut
from api.api_v1_schema import UserSchema
from api.models import Car
from api.models import Garage

app = NinjaAPI(
    title="Django Ninja API Demo",
    version="1.0.0",
    csrf=True,
)


@app.get("/health")
def get_health(request):
    return 200, {"status": "ok"}


@app.get("/me", response={200: UserSchema, 403: ErrorOut}, url_name="get_me")
def get_me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Not authenticated"}
    return request.user


@app.get("/cars", response={200: List[CarOut], 403: ErrorOut}, url_name="get_cars")
def get_cars(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Not authenticated"}
    return Car.objects.all()


@app.get("/cars/{id}", response={200: CarOut, 403: ErrorOut}, url_name="get_car")
def get_car(request, id):
    if not request.user.is_authenticated:
        return 403, {"message": "Not authenticated"}
    return Car.objects.get(id=id)


@app.post("/cars", response={201: CarOut, 403: ErrorOut}, url_name="post_car")
def post_car(request, payload: CarIn):
    if not request.user.is_authenticated:
        return 403, {"message": "Not authenticated"}
    car = Car.objects.create(**payload.dict())
    return 201, car


@app.get("/garages", response={200: List[GarageOut], 403: ErrorOut}, url_name="get_garages")
def get_garages(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Not authenticated"}
    return Garage.objects.all()
