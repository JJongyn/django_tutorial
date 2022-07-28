# Simple Registration tutorial with mysql
mysql을 이용한 간단한 회원가입 모델 구현입니다.
## Contents

1. [Connecting django with mysql](#connecting-django-and-mysql) 
2. [Create admin](#create-admin) 
3. [Create model](#create-model)
4. [Check mysql connection with admin](#check-mysql-connetion-with-admin)
## connecting django with mysql
- Create django project/app
```python
django-admin startproject "project name" 
django-admin startapp "app name"
```
- Conneting django with mysql
```python
# settings.py
# change DATABASES as below
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'put your mysql SCHEMAS name!!',  # 미리 SCHEMAS 만들어 놓아야 함.
        'USER':'root',
        'PASSWORD':'put you password !!',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
## create model
* Create simple Accounts model
```python
# models.py
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

```

* Add your models to admin
```python
# admin.py
from .models import Accounts

@admin.register(Accounts)
class UserAdmin(admin.ModelAdmin):
    # admin에서 보이는 field 지정
    list_display = ['user_id', 'user_name','user_email','user_created']
    
```

* Migrate updated models
```python
python manage.py makemigrations
python manag.py migrate # mysql workbench에 table 생겨야함!
```
## create admin
* Create admin account
```python
python manage.py createsuperuser

'''
Username (leave blank to use ' '): admin
Email address: admin@algomoa.com
Password:
Password (again):
'''
```

## check mysql connetion with admin
* Conneting to sever
```python
python manage.py runserver
```
1. http://127.0.0.1:8000/admin
2. Login with an admin account
3. Click [+Add] Next to your models name "Accountss"
4. Register user 
5. Check your mysql workbench(or shell) table
