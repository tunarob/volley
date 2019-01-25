from django.db import models
from django.conf import settings
from django_extensions.db.models import AutoSlugField, TimeStampedModel


class League(TimeStampedModel):
    name = models.CharField(
        max_length=60,
    )
    slug = AutoSlugField(
        populate_from=['name'],
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name
