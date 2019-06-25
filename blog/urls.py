from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('api/posts/', views.ApiPostList.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', views.ApiPostDetail.as_view(), name='api_post_detail'),
    path('api/', views.api_root),
]
