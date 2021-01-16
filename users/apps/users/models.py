from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    username = models.CharField('Usuario', max_length=10, unique=True)
    email = models.EmailField('Correo electrónico')
    names = models.CharField('Nombres', max_length=30, blank=True)
    last_names = models.CharField('Apellidos', max_length=30, blank=True)
    gender = models.CharField('Género', max_length=1, choices=GENDER_CHOICES, blank=True)
    register_code = models.CharField('Código de registro', max_length=6, blank=True)

    is_staff = models.BooleanField('Acceso a administrador', default=False)
    is_active = models.BooleanField('Activo', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]


    objects = UserManager()

    def __str__(self):
        return str(self.id) + ' ' + self.username

    def get_short_name(self):
        return str(self.id) + ' ' + self.username

    def get_full_name(self):
        return str(self.id) + ' ' + self.names + ' ' + self.last_names