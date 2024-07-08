from django import forms
from .models import WeightEntry, Exercise


class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ["weight"]


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "name",
            "image",
            "is_public",
            "main_muscle_group",
            "secondary_muscle_groups",
        ]
        widgets = {
            "main_muscle_group": forms.Select(choices=Exercise.MUSCLE_GROUPS),
            "secondary_muscle_groups": forms.SelectMultiple(
                choices=Exercise.MUSCLE_GROUPS
            ),
        }
