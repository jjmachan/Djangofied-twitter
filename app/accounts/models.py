from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)
    tweet_date = models.DateTimeField('date tweeted',
                            default=timezone.now)
    tweet_likes = models.IntegerField(default=0)
    tweet_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet_text
