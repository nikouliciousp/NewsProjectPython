from news.models import Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleListSerializer


class ArticleListCreateAPIView(APIView):
    """
    API view for listing all active articles and creating new articles.
    """

    def get(self, request):
        """
        Handle GET requests to retrieve a list of all active articles.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A Response object with serialized data of active articles and HTTP 200 status.
        """
        articles = Article.objects.filter(active=True)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new article.

        Args:
            request: The HTTP request object containing article data.

        Returns:
            Response: A Response object with serialized data of the created article and HTTP 201 status,
                      or HTTP 400 status with validation errors.
        """
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a specific article by its ID.
    """

    def get_object(self, pk):
        """
        Retrieve a specific article by its primary key.

        Args:
            pk: The primary key of the article to retrieve.

        Returns:
            Article: The article instance if found.

        Raises:
            Http404: Raises Http404 if the article is not found.
        """
        from django.shortcuts import get_object_or_404
        return get_object_or_404(Article, pk=pk, active=True)

    def get(self, request, pk):
        """
        Handle GET requests to retrieve a specific article by its primary key.

        Args:
            request: The HTTP request object.
            pk: The primary key of the article to retrieve.

        Returns:
            Response: A Response object with serialized data of the requested article and HTTP 200 status.
        """
        article = self.get_object(pk)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Handle PUT requests to update a specific article.

        Args:
            request: The HTTP request object containing updated article data.
            pk: The primary key of the article to update.

        Returns:
            Response: A Response object with serialized data of the updated article and HTTP 200 status,
                      or HTTP 400 status with validation errors.
        """
        article = self.get_object(pk)
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a specific article.

        Args:
            request: The HTTP request object.
            pk: The primary key of the article to delete.

        Returns:
            Response: A Response object with HTTP 204 status indicating successful deletion.
        """
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
