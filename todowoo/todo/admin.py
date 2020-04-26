from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

#register the to do model we just createed in models.py
admin.site.register(Todo, TodoAdmin)


