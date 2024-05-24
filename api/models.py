from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    capacity = models.IntegerField()
    capacity_unit = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"sample_schema"."car"'

    def __str__(self):
        return self.name


class Garage(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()  # ガレージの総容量
    cars = models.ManyToManyField("Car", related_name="garages")  # ガレージに含まれる車

    class Meta:
        db_table = '"sample_schema"."garage"'

    def __str__(self):
        return self.name


class CarGarage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    parked_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=100, null=True, blank=True)  # 車の位置情報など追加情報

    class Meta:
        unique_together = ("car", "garage")
        db_table = '"sample_schema"."car_garage"'

    def __str__(self):
        return f"{self.car.name} in {self.garage.name}"
