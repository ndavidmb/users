from django.db import models
#
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser,is_active, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username,
            email,
            password,
            False,
            False,
            False,
            ** extra_fields,
        )

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username,
            email,
            password,
            True,
            True,
            True,
            **extra_fields
        )

    def code_validation(self, id_user, cod_register):
        if self.filter(id=id_user, register_code=cod_register).exists():
            return True
        else:
            return False