from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index),
    path('', views.singapore_population)
]
