from django.contrib import admin

# Register your models here.
from check.core.models import Cliente, User

admin.site.register(Cliente)
admin.site.register(User)