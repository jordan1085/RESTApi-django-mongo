from django.contrib import admin
from .models import Book
# Register your models here.
# Cada vez que se crea u nuevo modelo debemos registrarlo para que se vea en adminApp
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass