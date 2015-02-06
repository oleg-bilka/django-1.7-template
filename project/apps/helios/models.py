from django.db import models

# Create your models here.

class HTTPRequest(models.Model):
    METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    )
    url = models.CharField(max_length=512, blank=False, null=False, unique=True, verbose_name="URL")
    duration = models.IntegerField(verbose_name="Duration(ms)")
    method = models.CharField(max_length=32, choices=METHOD_CHOICES)

    class Meta:
        verbose_name = 'HTTP Request'