from django.urls import path

from .views import ArticleListCreateAPIView, ArticleDetailAPIView

urlpatterns = [
    # URL pattern for listing all articles and creating a new article
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    # URL pattern for retrieving, updating, and deleting a specific article by its ID
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
]
