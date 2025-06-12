from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Sticky Notes REST API",
      default_version='v1',
      description="A Django REST Framework Backend for Managing Sticky Notes with Tagging, Filtering, and Search Functionality.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('stickynotes/api/',include('restapi.urls'))
]
