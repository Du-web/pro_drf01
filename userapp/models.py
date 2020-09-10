from django.db import models

# Create your models here.


class User(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'other')
    )
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    email = models.CharField(max_length=40)

    class Meta:
        db_table = 'db_user'