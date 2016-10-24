from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers.users import UserManager


def profile_avatar_to(instance, filename):
    return u'uploads/users/{user_id}/avatars/{filename}'.format(
        user_id=instance.id,
        filename=filename
    )


class Phone(models.Model):
    name = models.CharField(max_length=20, choices=[
        (1, _(u'Cellphone')),
        (2, _(u'Home')),
        (3, _(u'Other')),
    ], default=None, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __unicode__(self):
        return self.phone


class Profile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Profile - Users'

    gender = models.CharField(max_length=6, choices=[
        ('Male', _(u'Male')),
        ('Female', _(u'Female'))
    ], default=None, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phones = models.ManyToManyField(Phone, blank=True)


    #Saves a phone
    def save_phone(self, type, phone_number, pk=None):
        phone = None
        if pk:
            try:
                phone = Phone.objects.get(pk=pk)
            except Exception, e:
                phone = None
        if not phone:
            phone = Phone()
        phone.phone = phone_number
        phone.name = type
        phone.save()
        self.phones.add(phone)
        return phone


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name_plural = 'Users'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    avatar = models.ImageField(upload_to=profile_avatar_to, blank=True, null=True, default=None)
    profile = models.OneToOneField(Profile, blank=True, null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_first_letter(self):
        return self.first_name[:1]

    def get_full_name(self):
        return u'{first_name} {last_name}'.format(
            first_name=self.first_name, 
            last_name=self.last_name)


    def serialize(self):
        return {
            'email' : self.email,
        }

    def save(self, *args, **kwargs):
        avatar = None
        if not self.pk and self.avatar:
            avatar = self.avatar
            self.avatar = None
        super(User, self).save(*args, **kwargs)
        if avatar:
            self.avatar = avatar
            self.save()

