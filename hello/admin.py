from django.contrib import admin
from .models import Hello

@admin.register(Hello)
class HelloAdmin(admin.ModelAdmin):
    pass
