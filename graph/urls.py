
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.Graph.as_view(), name='test'),
    path('final/', views.final, name='final' ),

]