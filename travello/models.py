from django.db import models
class prac(models.Model):
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'pics')
    postby = models.CharField(max_length=100)
    like = models.IntegerField()
    com = models.IntegerField()
    dest = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
# Create your models here.
