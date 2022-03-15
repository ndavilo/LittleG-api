from django.db import models

# Create your models here.

class LittleG(models.Model):
	problem = models.CharField(max_length=100)
	solution = models.CharField(max_length=100)
	datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.problem
