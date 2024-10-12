from django.contrib import admin
from .models import Suport

@admin.register(Suport)
class SupportAdmin(admin.ModelAdmin):
    pass