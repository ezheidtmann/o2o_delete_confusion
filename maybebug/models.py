from __future__ import unicode_literals

from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=255)

class ThingAttachment(models.Model):
    thing = models.OneToOneField(Thing, related_name='attachment')
    name = models.CharField(max_length=255)
