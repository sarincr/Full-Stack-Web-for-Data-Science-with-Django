# import the standard Django Model
# from built-in library
from django.db import models



class apponemodel(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	last_modified = models.DateTimeField(auto_now_add=True)
