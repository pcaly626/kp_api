from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_connection),
    path('sinapore_population',views.sinapore_population),
    path('data_schema',views.data_schema),
    path('artists', views.artists),
    path('list',views.list_functions)
]
