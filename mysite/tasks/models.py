from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    description = models.CharField(max_length=100, default="No description")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title