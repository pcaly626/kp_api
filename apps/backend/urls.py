from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sinapore_population',views.sinapore_population),
    path('next_dataset',views.next_dataset),
    path('list',views.list_functions),
    path('district/<int:id>', views.one_district)
]
