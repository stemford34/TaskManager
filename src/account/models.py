from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _


class User(AbstractBaseUser):
    email       = models.EmailField(_("Email field"), max_length=254, unique=True)
    full_name   = models.CharField(_("Full name"), max_length=254, blank=True, null=True)
    is_active   = models.BooleanField(_("Active flag"), default=True)
    timestamp   = models.DateTimeField(_("Registration time"), auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class EmailActivation(models.Model):
    user            = models.ForeignKey("account.User", verbose_name=_("User"), on_delete=models.CASCADE)
    email           = models.EmailField()
    key             = models.CharField(_("key"), max_length=120, blank=True, null=True)
    forced_expired  = models.BooleanField(default=False)
    expires         = models.IntegerField(default=7)
    activated       = models.BooleanField(_("Act"), default=False)
    timestamp       = models.DateTimeField(_("Registration time"), auto_now_add=True)
    timestamp       = models.DateTimeField(_("Update time"), auto_now=True)

    def __str__(self):
        return self.email
    