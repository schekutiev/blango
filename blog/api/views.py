from rest_framework import generics
from blango_auth.models import User
from blog.models import Post
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from rest_framework.authentication import SessionAuthentication
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject


class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer