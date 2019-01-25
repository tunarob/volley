from django.contrib import admin
from .models.league import League
from .models.match import Match
from .models.player import Player, PlayerInTeam
from .models.season import Season
from .models.team import Team, TeamSeason


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    pass


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamSeason)
class TeamSeasonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'team',
        'season',
    )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(PlayerInTeam)
class PlayerInTeamAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'team',
    )


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass
