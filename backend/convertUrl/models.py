from django.db import models

# Create your models here.
class React(models.Model):
    input_url = models.CharField(max_length=2048)