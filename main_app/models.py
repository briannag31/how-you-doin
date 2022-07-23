from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


MOODS = (
    ('G', 'Good Day'),
    ('O', 'OK Day'),
    ('B', 'Bad Day')
)
FEELINGS = (
    ('P', 'Positive'),
    ('N', 'Negative'),
    ('Ne', 'Neutral')
)

class Feeling(models.Model):
  name = models.CharField(max_length=50)
  designation = models.CharField(
    max_length=2,
    choices=FEELINGS,
    default=FEELINGS[0][0]
  )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('feelings_detail', kwargs={'pk': self.id})


class Mood(models.Model):
    date = models.DateField()
    headline = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    designation = models.CharField(
    max_length=1,
    choices=MOODS,
    default=MOODS[0][0])
    feelings = models.ManyToManyField(Feeling)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('detail', kwargs={'mood_id': self.id})
    
