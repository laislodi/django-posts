from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('create-user', views.UserListCreateView.as_view(), name='create_users'),
]
