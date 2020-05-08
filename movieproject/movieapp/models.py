from django.db import models

# Create your models here.
class movie(models.Model):
	relyear=models.IntegerField()
	movname=models.CharField(max_length=30)
	hero=models.CharField(max_length=30)
	heroine=models.CharField(max_length=30)
	rating=models.IntegerField()
