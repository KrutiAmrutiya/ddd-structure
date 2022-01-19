from django.db import models


# Create your models here.
class Task(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
