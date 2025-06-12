from django.urls import path
from restapi.views import NoteCR,NoteUD
urlpatterns = [
    path('cr/',NoteCR.as_view()),
    path('ud/<uuid:id>/',NoteUD.as_view())
]
