from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='dogme-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #линк към конкретен пост с ID / да се промени с името на поста в урл-то
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), #също като PostDetailView
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]
