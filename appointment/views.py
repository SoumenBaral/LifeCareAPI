from django.shortcuts import render
from . import models , serializers
from rest_framework import viewsets

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset() # Sob gula query nilam 6 no line thake 
        patient_id = self.request.query_params.get("patient_id")

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
    
    def get_queryset(self):
        queryset = super().get_queryset() # Sob gula query nilam 6 no line thake 
        doctor_id = self.request.query_params.get("doctor_id")

        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset
