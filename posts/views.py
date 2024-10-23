from rest_framework import generics

from .models import Post, Customer
from .serializers import PostRetrieveSerializer, PostCreateSerializer, CustomerSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-datetime')
    serializer_class = PostRetrieveSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all().order_by('-datetime')
    serializer_class = PostCreateSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
