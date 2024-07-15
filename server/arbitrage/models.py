from django.db import models
from django.utils import timezone

class ArbitrageOpportunity(models.Model):
    event_name = models.CharField(max_length=20)
    competitors = models.CharField(max_length=100)
    market = models.CharField(max_length=50)
    sides = models.JSONField(default=list)
    site_one_odds = models.DecimalField(max_digits=6, decimal_places=2)
    site_two_odds = models.DecimalField(max_digits=6, decimal_places=2)
    site_one_name = models.CharField(max_length=50)
    site_one_link = models.URLField(max_length=255)
    site_two_name = models.CharField(max_length=50)
    site_two_link = models.URLField(max_length=255)
    found = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    ended = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event_name} - {self.competitors}"
