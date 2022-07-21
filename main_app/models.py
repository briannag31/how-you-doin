from django.db import models

MOODS = (
    ('G', 'Good Day'),
    ('O', 'OK Day'),
    ('B', 'Bad Day')
)

class Mood(models.Model):
    date = models.DateField()
    headline = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    designation = models.CharField(
    max_length=1,
    choices=MOODS,
    default=MOODS[0][0]
  )


    def __str__(self):
        return self.headline
    
