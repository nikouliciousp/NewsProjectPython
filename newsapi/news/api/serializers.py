from django.utils.timesince import timesince
from news.models import Article, Journalist
from rest_framework import serializers


class ArticleListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Article model, including a calculated field
    to show the time since the article was published.
    """
    # Calculated field to show the time since publication
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'  # Include all fields of the Article model in the serialized output

    def get_time_since_publication(self, obj):
        """
        Calculate the time since the article was published.

        Args:
            obj: The Article instance being serialized.

        Returns:
            str: A human-readable string showing the elapsed time since publication,
                 or None if the publication date is not set.
        """
        publication_date = obj.publication_date  # Retrieve the publication date
        if publication_date:
            # Use Django's timesince utility to calculate time since publication
            time_since_publication = timesince(publication_date)
            return time_since_publication  # Return the calculated time
        return None

    def validate(self, data):
        """
        Validate the serialized data.

        Args:
            data (dict): Data being validated.

        Raises:
            serializers.ValidationError: If the title and description are the same.

        Returns:
            dict: The validated data.
        """
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and description cannot be the same.")
        return data

    def validate_title(self, value):
        """
        Validate the title field.

        Args:
            value (str): The title being validated.

        Raises:
            serializers.ValidationError: If the title is 'test'.

        Returns:
            str: The validated title.
        """
        if value.lower() == 'test':
            raise serializers.ValidationError("Title cannot be 'test'.")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Journalist model, including a relationship
    to the articles they have authored.
    """
    # Nested serializer to include the list of articles
    articles = ArticleListSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = '__all__'  # Include all fields of the Journalist model in the serialized output