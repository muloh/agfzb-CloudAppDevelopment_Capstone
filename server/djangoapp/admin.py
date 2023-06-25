from django.contrib import admin
from .models import *


# Register your models here.

# CarModelInline class

class CarModelInline(admin.TabularInline):
    model = CarModel

# @admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarDealer)
# admin.site.register(CarModel)

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
