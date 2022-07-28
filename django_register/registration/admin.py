from django.contrib import admin
from .models import Accounts

@admin.register(Accounts)
class UserAdmin(admin.ModelAdmin):
    # admin에서 보이는 field 지정
    list_display = ['user_id', 'user_name','user_email','user_created']
    