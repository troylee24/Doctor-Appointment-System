from django.db import models
from django.db.models.deletion import CASCADE
from .validators import validate_time_15
from django import forms

class Doctor(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Patient(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=CASCADE)
    patient = models.ForeignKey(Patient, on_delete=CASCADE)
    date = models.DateField()
    time = models.TimeField(validators=[validate_time_15])
    kind = models.CharField(
        max_length=60,
        choices=(
            ("NP", "New Patient"),
            ("FU", "Follow-up")
        )
    )
