from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, unique=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['sort']


class Portfolio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, unique=True, null=True )
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField(null=True)
    photo = models.ImageField(upload_to='portfolio', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ['name']


class About(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, unique=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField(null=True)
    photo = models.ImageField(upload_to='about', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['name']


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, unique=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField(null=True)
    photo = models.ImageField(upload_to='team', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['name']


class Contact(models.Model):
    tel_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                               message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.' )

    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    tel = models.CharField(max_length=20, validators=[tel_regex], unique=True, null=True)
    message = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-date_created']
