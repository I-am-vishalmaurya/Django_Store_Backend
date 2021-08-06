from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_models(obj_type)
        return TaggedItems.object.select_related('tag').filter(content_type=content_type, object_id=obj_id)


class Tags(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class TaggedItems(models.Model):
    object_id = TaggedItemManager()
    # What tags are applied to object
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # Type video, Product, article
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
