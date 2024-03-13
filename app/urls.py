from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'cars', views.CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("cars/<str:slug>", views.showFile, name="showFile"),
    path('', include(router.urls)),
]

urlpatterns += router.urls
