from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register("category", views.CategoryViewset)
router.register("flowers", views.FLowerViewset)
router.register("review", views.ReviewViewset)

urlpatterns = [
    path("", include(router.urls)),
]
