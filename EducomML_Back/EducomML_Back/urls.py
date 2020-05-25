
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('knowledgedomain', views.KnowledgedomainViewSet)
router.register('Module', views.ModuleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
