from django.shortcuts import render
from . import models , serializers
from rest_framework import viewsets,pagination,filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 #Item Per Page
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    search_fields =['user__first_name','user__email','designation__name','specialization__name']
    filter_backends =[filters.SearchFilter]
    pagination_class=DoctorPagination

    



class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
  
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer