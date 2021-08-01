from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Tags(models.Model):
    label = models.CharField(max_length=255)


class TaggedItems(models.Model):
    # What tags are applied to object
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # Type video, Product, article
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
