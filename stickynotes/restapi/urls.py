from django.urls import path
from restapi.views import NoteCR,NoteUD,SearchByTitle,SearchByContent,FilterByTags
urlpatterns = [
    path('cr/',NoteCR.as_view()),
    path('ud/<uuid:id>/',NoteUD.as_view()),
    path('search-by-title/<str:title>',SearchByTitle.as_view()),
    path('search-by-content/<str:content>',SearchByContent.as_view()),
    path('filter-by-tags/<str:tag>',FilterByTags.as_view())
]
