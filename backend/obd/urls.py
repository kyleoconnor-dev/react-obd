from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path('hello/', views.get_obd)
]