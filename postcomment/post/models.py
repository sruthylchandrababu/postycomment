from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    def __str__(self):
      return self.name
    post_name=models.CharField(max_length=100)
    post=models.CharField(max_length=500)
    date=models.DateField(default=datetime.date.today)
