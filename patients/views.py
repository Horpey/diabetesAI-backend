from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Patient

# Create your views here.

# In views.py
def patients_list(request):
    MAX_OBJECTS = 20
    patient = Patient.objects.all()[:MAX_OBJECTS]
    data = {"results": list(patient.values("patientName", "dateOfBirth", "gender"))}
    return JsonResponse(data)


def patients_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    data = {
        "results": {
            "patientName": patient.patientName,
            "dateOfBirth": patient.dateOfBirth.username,
            "created_by": patient.created_by,
            "pub_date": patient.pub_date,
            "gender": patient.gender,
        }
    }
    return JsonResponse(data)
