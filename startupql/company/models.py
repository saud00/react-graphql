from django.db import models
from django.conf import settings


# Create your models here.

class link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class title(models.Model):
    Title = models.TextField(blank=True)

    def __str__(self):
        return self.Title


class city(models.Model):
    City = models.TextField(blank=True)

    def __str__(self):
        return self.City

class Employ(models.Model):
    Name = models.TextField(blank=True)
    Link = models.ForeignKey(link, related_name='link', on_delete=models.CASCADE)
    E_city = models.ForeignKey(city, related_name='E_city', on_delete=models.CASCADE)
    E_title = models.ForeignKey(title, related_name='E_title', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

