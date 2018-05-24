from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User


class RegularUser(models.Model):
	gender_options = (
			('M', 'Male'),
			('F', 'Female'),
			('O', 'Other'),
		)
	user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
	name = models.CharField(max_length = 40)
	college = models.TextField()
	check = models.BooleanField(default = False)
	birthday = models.DateField(default = timezone.now)
	gender = models.CharField(max_length = 1, choices = gender_options, null = True)



	def __str__(self):
		return self.name

