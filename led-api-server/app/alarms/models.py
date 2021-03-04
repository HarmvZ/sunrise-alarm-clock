from django.db import models


class AlarmConfig(models.Model):
    colors = models.JSONField(help_text="List of colors to progress through")
    playlist = models.CharField(
        max_length=255, blank=True, help_text="Mopidy URI of playlist"
    )
    volumes = models.JSONField(
        help_text="List of (time, volume) tuples to progress through"
    )
    duration = models.IntegerField(help_text="Duration of wake up cycle in seconds")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]
