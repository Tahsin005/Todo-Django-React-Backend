from django.contrib import admin
from . models import Todo
# Register your models here.
@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'completed', 'updated', 'created']
    