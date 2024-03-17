from django.urls import path
from . import views

urlpatterns = [
    path('', views.printHeaders, name='headers'),
    path('a', views.testAsync, name='test'),
]
