from operator import mod
from django.db import models

# Create your models here.
class Accounts(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    user_pw = models.CharField(max_length=128)
    user_name = models.CharField(max_length=10)
    user_email = models.EmailField(max_length=128, unique=True)
    user_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
    # DB 네임 지정
    class Meta:
        db_table = "user"