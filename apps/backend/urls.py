from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_connection),
    path('sinapore_population',views.sinapore_population),
    path('next_dataset',views.next_dataset),
    path('artist', views.artists),
    path('list',views.list_functions)
]
