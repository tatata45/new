from django.db import models

class Acticle(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category_id = models.IntField()