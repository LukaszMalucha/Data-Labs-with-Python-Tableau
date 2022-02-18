from django.db import models
from django.contrib.auth.models import User
from core.utils import content_file_name


class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default='guest', blank=True)
    image = models.ImageField(upload_to=content_file_name, default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"


class DataSkill(models.Model):
    dataskill = models.CharField(max_length=255, blank=True)
    percentage = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return self.dataskill
