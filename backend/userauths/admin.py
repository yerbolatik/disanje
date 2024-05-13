from django.contrib import admin
from userauths.models import Profile, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']


class ProfieAdmin(admin.ModelAdmin):
    list_display = ['image', 'full_name', 'gender', 'country']
    list_editable = ['gender', 'country']
    search_fields = ['full_name']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfieAdmin)
