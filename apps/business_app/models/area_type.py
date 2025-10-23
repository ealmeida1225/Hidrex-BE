from django.db import models


class AreaType(models.Model):
    name = models.CharField(max_length=50)
    representation = models.CharField(max_length=7)
    description = models.TextField()

    def __str__(self):
        return self.name
