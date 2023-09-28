import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    medical_id = models.CharField(max_length=12, unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.medical_id:
            medical_id = str(uuid.uuid4())
            medical_id = medical_id.replace('-', '').upper()[:12]
            self.medical_id = medical_id  # Assign the generated medical_id to the object
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name
