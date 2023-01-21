from django.urls import path, include
from . import views
from home.views import home_API, person
urlpatterns = [
    path('home/', views.home),
    path('busqueda/', views.busqueda),
    path('api/home/', home_API),
    path('api/home/people', person),   
]
