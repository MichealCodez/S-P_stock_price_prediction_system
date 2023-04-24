from django.db import models

class Predictions(models.Model):
    stock = models.CharField(max_length=10, default="ES")
    pattern = models.CharField(max_length=500)
    open_p = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()

    def __str__(self):
        return str(self.id)