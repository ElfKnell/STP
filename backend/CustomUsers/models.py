from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


ROLE_CHOICES = (
    (0, 'admin'),
    (1, 'manager'),
    (2, 'visitor')
)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if validate_email(email):
            raise ValidationError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', 2)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', 0)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
            This class represents a basic user. \n
            Attributes:
            -----------
            param first_name: Describes first name of the user
            type first_name: str max length=20
            param last_name: Describes last name of the user
            type last_name: str max length=20
            param email: Describes the email of the user
            type email: str, unique, max length=100
            param password: Describes the password of the user
            type password: str
            param created_at: Describes the date when the user was created. Can't be changed.
            type created_at: int (timestamp)
            param updated_at: Describes the date when the user was modified
            type updated_at: int (timestamp)
            param is_staff: user is_staff, default is_staff (2, 'visitor')
            type updated_at: int (choices)
            param is_active: user is_staff, default value False
            type updated_at: bool

        """
    email = models.EmailField(_('email address'), unique=True, max_length=40,)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date updated'), default=None, null=True)
    is_staff = models.IntegerField(_('staff'), default=2, choices=ROLE_CHOICES)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
