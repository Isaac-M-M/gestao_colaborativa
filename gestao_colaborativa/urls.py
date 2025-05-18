from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import ProjetoViewSet


router = routers.DefaultRouter()
router.register(r'api/projetos', ProjetoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include(router.urls)),
]
