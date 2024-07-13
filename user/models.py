from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.urls import reverse
# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(blank=False, max_length=255)
    user_name = models.CharField(blank=False, max_length=255)
    profile_photo = models.ImageField(blank=False)


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username":self.user_name})