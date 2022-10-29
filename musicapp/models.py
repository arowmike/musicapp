from django.db import models
from django.conf import settings


# Create your models here.
class Artiste(models.Model):
    """A topic the user is learning about."""
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.PositiveIntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = f"{first_name} +{last_name}"

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date_released = models.BooleanField(default=False)
    likes = models.Aggregate
    artiste_id = models
    date_added = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title

class Lyric(models.Model):
    """Something specific learned about a topic."""
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    content = models.TextField()
    song_id = models
    date_added = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        """Return a string representation of the model."""
        return self.content