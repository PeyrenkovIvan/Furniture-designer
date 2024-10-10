from django.db import models


class Bed(models.Model):
	length = models.CharField(max_length=50)
	width = models.CharField(max_length=50)
	base = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	
	images = models.ImageField(upload_to='media/')


