from django.db import models


class PluviometerType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "research_pluviometertype"
        verbose_name = "Pluviometer type"
        verbose_name_plural = "Pluviometer types"

    def __str__(self):
        return self.name
