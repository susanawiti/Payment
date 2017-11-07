from django.db import models


#  Create your models here.
class Payment(models.Model):
    name =models.CharField(max_length=200)
    amount = models.IntegerField()
    product = models.TextField()
    
    def __str__(self):
        return self.name


    