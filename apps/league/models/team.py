from django.db import models
from django_extensions.db.models import AutoSlugField, TimeStampedModel


class Team(TimeStampedModel):
    name = models.CharField(
        max_length=60,
    )
    slug = AutoSlugField(
        populate_from=['name'],
    )
    location = models.TextField()

    def __str__(self):
        return self.name


class TeamSeason(TimeStampedModel):
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )
    season = models.ForeignKey(
        'league.Season',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=60,
    )
    slug = AutoSlugField(
        populate_from=['name'],
    )

    def __str__(self):
        return self.name
