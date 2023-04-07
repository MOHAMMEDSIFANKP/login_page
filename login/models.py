from django.db import models

# Create your models here.
class Login_part(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)


class cameras(models.Model):
    image = models.ImageField(upload_to="home")
    