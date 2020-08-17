from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Extend a standard users model with additional info
    I use a one-to-one relationship
    """

    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        UNDEFINED = 'U', _('Undefined')

    user = models.OneToOneField(User, verbose_name="Link to user", on_delete=models.CASCADE)
    sex = models.CharField(verbose_name="Sex",
                           max_length=1,
                           choices=Sex.choices,
                           default=Sex.UNDEFINED)
    age = models.PositiveSmallIntegerField(verbose_name='Age', null=True, blank=True)
