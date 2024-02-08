from django.db import models

# Create your models here.

class India(models.Model):
    Ind_state = models.CharField(max_length=100)
    Ind_city = models.CharField(max_length=100)
    Ind_code = models.IntegerField()
    def __str__(self):
        return self.Ind_state
    