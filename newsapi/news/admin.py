from django.contrib import admin

from .models import Article, Journalist

# Register the Article model with the admin site
admin.site.register(Article)

# Register the Journalist model with the admin site
admin.site.register(Journalist)
