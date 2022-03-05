from django.db import models
from django.contrib.auth.models import User
from .excuse_choices import categories

# Create your models here.

class UserExcuse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excuse_category = models.CharField(max_length=45, choices=categories)
    excuse = models.TextField()
    excuse_id = models.IntegerField()
    time_created = models.TimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "user_excuses"
