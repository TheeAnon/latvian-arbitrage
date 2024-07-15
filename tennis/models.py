from django.db import models

# Create your models here.
class Sites(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()


class Match(models.Model):
    event_name = models.CharField(max_length=255)
    competitors = models.CharField(max_length=255)
    is_live = models.BooleanField(default=False)
    date = models.DateTimeField()

