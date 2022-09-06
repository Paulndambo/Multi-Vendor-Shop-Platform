from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("prodiles", views.UserProfileViewSet, basename="profiles")

urlpatterns = [
    path("", include(router.urls)),
    #path("", views.UserAPIView.as_view({'get': 'list', 'post': 'create'}), name="users"),
    path("<int:pk>/", views.UserRetrieveUpdateAPIView.as_view(), name="users-detail"),
]
