from django.urls import path
from . import views
from core.views import index, generation, translate, text


urlpatterns = [
    path('', views.index, name='index'),
    path('caption/', views.generation, name='caption'),
    path('generation/', views.generation, name='text'),
    path('translate/', views.index, name='translate'),

]