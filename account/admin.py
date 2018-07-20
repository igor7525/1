from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from account.models import User as AccountUser, Group as AccountGroup

# Register your models here.
class AccountUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('avatar', 'first_name', 'last_name', 'email', 'phone', 'phone_2')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'position',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
     
admin.site.register(AccountUser, AccountUserAdmin)


class AccountGroupAdmin(GroupAdmin):
    pass

admin.site.unregister(Group)
admin.site.register(AccountGroup, AccountGroupAdmin)