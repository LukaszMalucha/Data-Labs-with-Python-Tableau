from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('User must have a valid email address')
        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Customized user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class DataSkill(models.Model):
    dataskill = models.CharField(max_length=255, blank=True)
    percentage = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return self.dataskill















