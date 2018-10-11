from __future__ import unicode_literals

from django.db import models
from .mocks import *

# Create your models here.
class Flight(models.Model):
    flight_no = models.CharField(max_length=5)
    depart_city = models.CharField(max_length=20)
    destination_city = models.CharField(max_length=20)
    date = models.DateField(auto_now=False, auto_now_add=False)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(choices=STATUS_CHOICES, default = LANDED, max_length=10)

    def __unicode__(self):
        return self.flight_no

    def __str__(self):
        return self.flight_no