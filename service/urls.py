from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceUsViewSet
router = DefaultRouter() # Our Router
router.register(r'', ServiceUsViewSet) # Antenna Of Router
urlpatterns = [
    path('',include(router.urls))

]
