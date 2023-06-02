from django.db import models

# Create your models here.
class Tavarlar(models.Model):
    nomi=models.CharField(max_length=200)
    narxi=models.FloatField()
    rasmi=models.FileField(upload_to="media")

    def __str__(self):
        return self.nomi