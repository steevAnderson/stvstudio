from django.contrib import admin

from .models import cliente, conocimiento, proyecto

# Register your models here.

admin.site.register(cliente)
admin.site.register(conocimiento)
admin.site.register(proyecto)