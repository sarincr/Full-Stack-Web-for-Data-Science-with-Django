from django.db import models


class Company(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    salary = models.IntegerField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name 