from django.db import models


class AnimeDB(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    img = models.CharField(max_length=30)
    genres = models.CharField(max_length=300)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return self.title
