from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stickynotes/api/',include('restapi.urls'))
]
