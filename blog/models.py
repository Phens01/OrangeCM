from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
	username = models.TextField()
	surname = models.TextField()
	age = models.TextField(max_length=4)
	nationality = models.TextField()
	cni = models.TextField(max_length=12)
	town = models.TextField()

	def __str__(self):
		return self.username

class Client(models.Model):
	agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
	username = models.TextField()
	surname = models.TextField()
	age = models.TextField(max_length=4)
	nationality = models.TextField()
	town = models.TextField()
	cni = models.TextField(max_length=12)
	date_added = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.username

	class Meta:
		ordering = ['-date_added']
