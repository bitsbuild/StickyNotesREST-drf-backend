from django.urls import path
from restapi.views import NoteCUD
urlpatterns = [
    path('create-update-delete/<uuid:id>/',NoteCUD.as_view())
]
