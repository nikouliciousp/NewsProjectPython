from django.urls import path

from .views import ArticleListCreateAPIView, ArticleDetailAPIView, JournalistListCreateAPIView, JournalistDetailAPIView

urlpatterns = [
    # URL pattern for listing all articles and creating a new article
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    # URL pattern for retrieving, updating, and deleting a specific article by its ID
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('journalists/', JournalistListCreateAPIView.as_view(), name='journalist-list'),
    path('journalists/<int:pk>/', JournalistDetailAPIView.as_view(), name='journalist-detail'),
]
