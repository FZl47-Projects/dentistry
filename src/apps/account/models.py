from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from model_utils.managers import InheritanceManager

from phonenumber_field.modelfields import PhoneNumberField

from apps.core.models import BaseModel


class CustomBaseUserManager(InheritanceManager, BaseUserManager):

    def get(self, *args, **kwargs):
        return self.get_subclass(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().select_subclasses()

    def create_superuser(self, phonenumber, password, **extra_fields):
        u = SuperUser.objects.create(
            phonenumber=phonenumber, **extra_fields
        )
        u.set_password(password)
        u.save()
        return u


class BaseUser(BaseModel, AbstractBaseUser):
    _role = None

    first_name = models.CharField(_('first name'), max_length=150, blank=True, default=_('no name'))
    last_name = models.CharField(_('last name'), max_length=150, blank=True, null=True)
    phonenumber = PhoneNumberField(_('phonenumber'), region='IR', unique=True)
    is_phonenumber_confirmed = models.BooleanField(_('phonenumber is confirmed'), default=False)
    is_active = models.BooleanField(_("active"), default=True, )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "phonenumber"
    REQUIRED_FIELDS = []

    objects = CustomBaseUserManager()

    class Meta:
        ordering = '-id',
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f'{self.phonenumber}'

    def get_raw_phonenumber(self):
        p = str(self.phonenumber).replace('+98', '')
        return p

    def get_role(self):
        return self._role


class SuperUser(BaseUser, PermissionsMixin):
    _role = models.CharField(_('role'), max_length=10, default='super_user')
    is_staff = models.BooleanField(_('is staff'), default=True, editable=False)
    is_superuser = models.BooleanField(_('is superuser'), default=True, editable=False)

    class Meta:
        verbose_name = _("super user")
        verbose_name_plural = _("super users")


class DoctorUser(BaseUser):
    _role = models.CharField(_('role'), max_length=12, default='doctor_user')
    city = models.CharField(_('city'), max_length=50)
    expertise = models.CharField(_('expertise'), max_length=100)

    class Meta:
        verbose_name = _("doctor user")
        verbose_name_plural = _("doctor users")


class CommonUser(BaseUser):
    _role = models.CharField(_('role'), max_length=12, default='common_user')
    city = models.CharField(_('city'), max_length=50)
    national_id = models.CharField(max_length=10)

    class Meta:
        verbose_name = _("common user")
        verbose_name_plural = _("common users")
