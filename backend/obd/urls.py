from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path('getObdData', views.get_obd)
]