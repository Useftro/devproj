from django.contrib import admin
from mapapp.models import Point


# Register your models here.
@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    pass
