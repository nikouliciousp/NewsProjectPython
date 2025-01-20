from news.models import Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleListSerializer, JournalistSerializer
from ..models import Journalist


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
        articles = Article.objects.filter(active=True)  # Retrieve all articles marked as active
        serializer = ArticleListSerializer(articles, many=True)  # Serialize the articles
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with HTTP 200 status

    def post(self, request):
        """
        Handle POST requests to create a new article.

        Args:
            request: The HTTP request object containing article data.

        Returns:
            Response: A Response object with serialized data of the created article and HTTP 201 status,
                      or HTTP 400 status with validation errors.
        """
        serializer = ArticleListSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():  # Validate the deserialized data
            serializer.save()  # Save the new article instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created article instance
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any


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
        return get_object_or_404(Article, pk=pk, active=True)  # Fetch the active article or raise 404

    def get(self, request, pk):
        """
        Handle GET requests to retrieve a specific article by its primary key.

        Args:
            request: The HTTP request object.
            pk: The primary key of the article to retrieve.

        Returns:
            Response: A Response object with serialized data of the requested article and HTTP 200 status.
        """
        article = self.get_object(pk)  # Retrieve the requested article
        serializer = ArticleListSerializer(article)  # Serialize the article data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with HTTP 200 status

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
        article = self.get_object(pk)  # Retrieve the article instance
        serializer = ArticleListSerializer(article,
                                           data=request.data)  # Deserialize input data with the article instance
        if serializer.is_valid():  # Validate the deserialized data
            serializer.save()  # Update the article instance
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated article data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any

    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a specific article.

        Args:
            request: The HTTP request object.
            pk: The primary key of the article to delete.

        Returns:
            Response: A Response object with HTTP 204 status indicating successful deletion.
        """
        article = self.get_object(pk)  # Retrieve the article to delete
        article.delete()  # Delete the article
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return no content response


class JournalistListCreateAPIView(APIView):
    """
    API view for listing all journalists and creating new ones.
    """

    def get(self, request):
        """
        Handle GET requests to retrieve a list of all journalists.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A Response object with serialized data of all journalists and HTTP 200 status.
        """
        journalists = Journalist.objects.all()  # Retrieve all journalist instances
        serializer = JournalistSerializer(journalists, many=True)  # Serialize the journalist data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with HTTP 200 status

    def post(self, request):
        """
        Handle POST requests to create a new journalist.

        Args:
            request: The HTTP request object containing journalist data.

        Returns:
            Response: A Response object with serialized data of the created journalist and HTTP 201 status,
                      or HTTP 400 status with validation errors.
        """
        serializer = JournalistSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():  # Validate the deserialized data
            serializer.save()  # Save the new journalist instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created journalist instance
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any


class JournalistDetailAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a specific journalist by their ID.
    """

    def get_object(self, pk):
        """
        Retrieve a specific journalist by their primary key.

        Args:
            pk: The primary key of the journalist to retrieve.

        Returns:
            Journalist: The journalist instance if found.

        Raises:
            Http404: Raises Http404 if the journalist is not found.
        """
        from django.shortcuts import get_object_or_404
        return get_object_or_404(Journalist, pk=pk)  # Fetch the journalist or raise 404

    def get(self, request, pk):
        """
        Handle GET requests to retrieve a specific journalist by their primary key.

        Args:
            request: The HTTP request object.
            pk: The primary key of the journalist to retrieve.

        Returns:
            Response: A Response object with serialized data of the requested journalist and HTTP 200 status.
        """
        journalist = self.get_object(pk)  # Retrieve the requested journalist
        serializer = JournalistSerializer(journalist)  # Serialize the journalist data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with HTTP 200 status

    def put(self, request, pk):
        """
        Handle PUT requests to update a specific journalist.

        Args:
            request: The HTTP request object containing updated journalist data.
            pk: The primary key of the journalist to update.

        Returns:
            Response: A Response object with serialized data of the updated journalist and HTTP 200 status,
                      or HTTP 400 status with validation errors.
        """
        journalist = self.get_object(pk)  # Retrieve the journalist instance
        serializer = JournalistSerializer(journalist,
                                          data=request.data)  # Deserialize input data with journalist instance
        if serializer.is_valid():  # Validate the deserialized data
            serializer.save()  # Update the journalist instance
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated journalist data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any

    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a specific journalist.

        Args:
            request: The HTTP request object.
            pk: The primary key of the journalist to delete.

        Returns:
            Response: A Response object with HTTP 204 status indicating successful deletion.
        """
        journalist = self.get_object(pk)  # Retrieve the journalist to delete
        journalist.delete()  # Delete the journalist
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return no content response
