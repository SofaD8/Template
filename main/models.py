from django.db import models


# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, unique=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Services'
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
    name = models.CharField(max_length=100, unique=True)