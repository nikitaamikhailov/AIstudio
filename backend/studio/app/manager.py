from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, login, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not login:
            raise ValueError(_('The Email must be set'))
        login = self.normalize_email(login)
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not phone:
            raise ValueError("User must have a full name")

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.model(
            email=self.normalize_email(email)
        )
        user.phone = phone
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save()
        return user


    def create_staffuser(self, login, password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user=self._create_user(login, password, True, False, **extra_fields)
        user.save(using=self._db)
        return user