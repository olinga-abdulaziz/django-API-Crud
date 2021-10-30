from django.db import models

# Create your models here.


class Students(models.Model):
    sname = models.CharField(max_length=100)
    dorm = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.sname
