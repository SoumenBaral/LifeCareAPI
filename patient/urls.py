from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet,UserRegistrationApiView
router = DefaultRouter() # Our Router
router.register(r'list', PatientViewSet) # Antenna Of Router

urlpatterns = [
    path('',include(router.urls)),
    path('register/',UserRegistrationApiView.as_view(),name='register')

]