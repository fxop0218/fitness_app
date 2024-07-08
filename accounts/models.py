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


class Exercise(models.Model):
    MUSCLE_GROUPS = [
        ("hombros", "Hombros"),
        ("trapecios", "Trapecios"),
        ("pecho", "Pecho"),
        ("dorsal", "Dorsal"),
        ("espalda alta", "Espalda Alta"),
        ("triceps", "Tríceps"),
        ("biceps", "Bíceps"),
        ("abductor", "Abductor"),
        ("gluteo", "Glúteo"),
        ("cuadriceps", "Cuádriceps"),
        ("abdominal", "Abdominal"),
        ("lumbar", "Lumbar"),
        ("gemelo", "Gemelo"),
        ("femoral", "Femoral"),
        ("antebrazo", "Antebrazo"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="exercise_images/", null=True, blank=True)
    is_public = models.BooleanField(default=False)
    main_muscle_group = models.CharField(max_length=20, choices=MUSCLE_GROUPS)
    secondary_muscle_groups = models.CharField(
        max_length=200, choices=MUSCLE_GROUPS, blank=True
    )

    def __str__(self):
        return self.name
