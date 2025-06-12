from django.urls import path
from restapi.views import NoteCRUD
urlpatterns = [
    path('crud/<uuid:id>/',NoteCRUD.as_view())
]
