from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)


class WeightEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.weight} kg on {self.date}"
