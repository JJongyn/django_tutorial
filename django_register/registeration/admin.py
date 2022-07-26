from django.contrib import admin
from .models import Accounts


# User모델 admin에서 확인하려고
@admin.register(Accounts)
class UserAdmin(admin.ModelAdmin):
    displaying = (
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_updated'
    )