from django.contrib import admin

from api.models import Car, Garage, CarGarage


class CarAdmin(admin.ModelAdmin):
    pass


class GarageAdmin(admin.ModelAdmin):
    pass


class GarageCarAdmin(CarAdmin, GarageAdmin):
    pass


admin.site.register(Car, CarAdmin)
admin.site.register(Garage, GarageAdmin)
admin.site.register(CarGarage, GarageCarAdmin)
