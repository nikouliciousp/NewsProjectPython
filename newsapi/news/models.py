from django.db import models


# Create your models here.
class Journalist(models.Model):
    """
    Represents a journalist who can author articles.
    """
    first_name = models.CharField(max_length=50)  # First name of the journalist
    last_name = models.CharField(max_length=50)  # Last name of the journalist
    biography = models.TextField(null=True, blank=True)  # Biography of the journalist (optional)

    def __str__(self):
        """
        Returns the full name of the journalist.
        """
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    """
    Represents a news article authored by a journalist.
    """
    # Foreign key to link the article to a journalist; allows cascading delete
    author = models.ForeignKey('Journalist', on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)  # Title of the article
    description = models.TextField()  # Short description or summary of the article
    body = models.TextField()  # Main content of the article
    location = models.CharField(max_length=50)  # Location related to the article
    publication_date = models.DateTimeField()  # Date when the article was published
    active = models.BooleanField(default=True)  # Indicates if the article is active and visible
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the article was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update of the article

    def __str__(self):
        """
        Returns the title of the article along with its author's name.
        """
        return f"{self.title} by {self.author}"
