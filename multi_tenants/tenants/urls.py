from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,MediaViewSet,TenantViewSet

router=DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'media',MediaViewSet)
router.register(r'tenants',TenantViewSet)

urlpatterns=[
    path('',include(router.urls)),
]