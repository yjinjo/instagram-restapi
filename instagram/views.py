from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    # 최소 2가지를 해줘야 합니다.
    queryset = Post.objects.all()  # 1. 데이터의 범위를 지정해줘야합니다.
    serializer_class = PostSerializer  # 2. Serializer Class를 지정해줘야합니다.
