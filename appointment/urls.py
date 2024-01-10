from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet
router = DefaultRouter() # Our Router
router.register(r'list', AppointmentViewSet) # Antenna Of Router
urlpatterns = [
    path('',include(router.urls))

]