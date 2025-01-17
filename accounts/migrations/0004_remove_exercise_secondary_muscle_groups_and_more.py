# Generated by Django 5.0.6 on 2024-07-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_secondarymusclegroup_exercise"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exercise",
            name="secondary_muscle_groups",
        ),
        migrations.DeleteModel(
            name="SecondaryMuscleGroup",
        ),
        migrations.AddField(
            model_name="exercise",
            name="secondary_muscle_groups",
            field=models.CharField(
                blank=True,
                choices=[
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
                ],
                max_length=200,
            ),
        ),
    ]
