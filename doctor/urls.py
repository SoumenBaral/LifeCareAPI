from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() # Our Router
router.register(r'list', views.DoctorViewSet) # Antenna Of Router
router.register(r'designation', views.DesignationViewSet)
router.register(r'specialization', views.SpecializationViewSet)
router.register(r'availableTime', views.AvailableTimeViewSet)
router.register(r'review', views.ReviewViewSet)
urlpatterns = [
    path('',include(router.urls))

]