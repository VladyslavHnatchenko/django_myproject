from django.db import models


class DreamReal(models.Model):
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    class Meta:
        db_table = "dreamreal"
