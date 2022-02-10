from django.urls import path
from . import views

# Define url patterns
urlpatterns = [
    path('', views.index),
    path('<int:confirmation_number>/', views.ticket_search),
]
