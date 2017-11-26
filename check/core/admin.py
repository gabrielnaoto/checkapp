from django.contrib import admin

# Register your models here.
from check.core.models import Cliente, User, Empresa, Fornecedor
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Empresa'), {'fields': ('empresa', )}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'empresa', 'password1', 'password2')}
         ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Empresa)
