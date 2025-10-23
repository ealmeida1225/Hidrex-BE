from django.db import models


class DiaryPrecipitationClassification(models.Model):
    lower_limmit = models.FloatField(blank=True, null=True)
    upper_limmit = models.FloatField(blank=True, null=True)
    classification = models.CharField(max_length=20)

    class Meta:
        db_table = "research_diaryprecipitationclassification"
