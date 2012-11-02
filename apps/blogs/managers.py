"""
The manager class for the blog models
"""
from datetime import datetime
from django.db import models
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q


class BlogPostQuerySet(QuerySet):
    def published(self):
        """
        Return only published entries
        """
        from .models import BlogPost # the import can't be globally, that gives a circular dependency
        return self\
            .filter(status=BlogPost.PostStatus.published)\
            .filter(
                Q(publication_date__isnull=True) |
                Q(publication_date__lte=datetime.now())
            ).filter(
                Q(publication_end_date__isnull=True) |
                Q(publication_end_date__gte=datetime.now())
            )



class BlogPostManager(models.Manager):
    """
    Extra methods attached to ``Entry.objects`` .
    """
    def get_query_set(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        """
        Return only published entries
        """
        return self.get_query_set().published()