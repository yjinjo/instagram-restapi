from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    "post", views.PostViewSet
)  # 2개의 URL을 만들어줍니다. (router.urls에 리스트 형태로 존재합니다.)

urlpatterns = [
    path("", include(router.urls)),
]
