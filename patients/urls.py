from django.urls import include, re_path, path
from .views import patients_list, patients_detail

urlpatterns = [
    re_path(r"^", include("patients.urls")),
    path("patients/", patients_list, name="patients_list"),
    path("patients/<int:pk>/", patients_detail, name="patients_detail"),
]
