from django.db import models

# Create your models here.

class BlogData(models.Model):
	title = models.CharField(max_length=200)
	title_link = models.URLField()
	description = models.TextField()
	date = models.DateField()
