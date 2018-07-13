from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    SEX = (
    ('F', 'Female'),
    ('M', 'Male'),
    )
    pub_date = models.DateField( editable=False, auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    gender = models.CharField(max_length=1,choices=SEX)

    def __str__(self):
        return self.first_name
