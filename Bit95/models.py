from django.db import models
from datetime import datetime

# Create your models here.
class Files(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, default="Text Document")
    data = models.TextField(max_length=16383, blank=True)
    date_time_created = models.CharField(max_length=64, default=datetime.now().strftime('%d/%m/%y'))

class Deleted_Files(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, default="Text Document")
    data = models.TextField(max_length=16383, blank=True)
    date_time_created = models.CharField(max_length=64)
    date_deleted = models.CharField(max_length=64, default=datetime.now().strftime('%d/%m/%y'))

