from django.db import models


class DreamReal(models.Model):
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    online = models.ForeignKey("Online", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dreamreal"


class Online(models.Model):
    domain = models.CharField(max_length=30)

    def __str__(self):
        return self.domain

    class Meta:
        db_table = "online"
