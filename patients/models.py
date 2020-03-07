from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
)


class Patient(models.Model):
    patientName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patientName
