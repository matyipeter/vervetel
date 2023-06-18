from django.db import models

# Create your models here.

class Patients(models.Model):

    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email = models.EmailField(default='xy@gmail.com')
    phone_num = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class DateTimes(models.Model):

    all_date = models.DateField()
    all_time = models.TimeField()

    

