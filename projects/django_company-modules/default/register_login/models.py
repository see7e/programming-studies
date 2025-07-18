from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subgroup = models.ManyToManyField('CustomSubGroup', related_name='users', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email} - {self.subgroup}'
    
    def has_module_perms(self, app_label):
        return self.is_staff


class CustomGroup(Group):
    # Add your additional fields here
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='managed_groups')
    
    class Meta:
        verbose_name = 'Custom Group'
        verbose_name_plural = 'Custom Groups'


class CustomSubGroup(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='managed_subgroups')
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name} - {self.manager} - {self.group}'
    

class Menu(models.Model):
    menu = models.CharField(max_length=50)
    submenu = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=100, null=True)
    group = models.ForeignKey(CustomGroup, on_delete=SET_NULL, blank=True, null=True)
    subgroup = models.ForeignKey(CustomSubGroup, on_delete=SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.menu} - {self.submenu} - {self.url}'
