from django.db import models
from django_extensions.db.models import TimeStampedModel


class Match(TimeStampedModel):
    SCORE_CHOICES = (
        (1, '3-0'),
        (2, '3-1'),
        (3, '3-2'),
        (4, '2-3'),
        (5, '1-3'),
        (6, '0-3'),
    )

    host = models.ForeignKey(
        'league.TeamSeason',
        on_delete=models.PROTECT,
        related_name='+',
    )
    guest = models.ForeignKey(
        'league.TeamSeason',
        on_delete=models.PROTECT,
        related_name='+',
    )
    match_date = models.DateTimeField()
    score = models.PositiveSmallIntegerField(
        choices=SCORE_CHOICES,
    )

    def __str__(self):
        return f'{self.host} ({self.get_score_display()}) {self.guest}'
