from django.shortcuts import render
from . import models , serializers
from rest_framework import viewsets

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

    



class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer