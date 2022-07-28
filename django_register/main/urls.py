
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls'))
    # path('', RedirectView.as_view(url="/home/", permanent=True)) <- home으로 바로 이동
]
