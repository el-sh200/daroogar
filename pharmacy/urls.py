from django.urls import path
from . import views

app_name = 'pharmacy'

urlpatterns = [
    path('', views.index, name='index'),
    path('send_data/', views.send_data, name='send_data'),
    path('generate/', views.generate_prescription, name='generate_prescription'),
]
