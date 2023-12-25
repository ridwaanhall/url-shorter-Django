# models.py
from django.db import models
from django.core.validators import RegexValidator

class UrlShortener(models.Model):
    target_url = models.URLField()
    short_url = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9]+$',
                message='Short URL can only contain letters and numbers.',
            ),
        ],
    )
