from django.urls import path
from . import views

# Define url patterns
urlpatterns = [
    path('', views.index),
    path('search/<str:origin>/<str:destination>/', views.flight_search),
]
