from django.contrib import admin

# Register your models here.
from check.core.models import Cliente, User, Empresa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Cliente)


class UserAdmin(BaseUserAdmin):
    pass
    # fieldsets = (u'Perfil do usuário', {'fields': ('empresa',)}),


admin.site.register(User, UserAdmin)
admin.site.register(Empresa)
