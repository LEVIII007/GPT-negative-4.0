from django.urls import path
from . import views
from core.views import index,translate, text, generation


urlpatterns = [
    path('', views.index, name='index'),
    path('caption/', views.caption, name='caption'),
    path('generation/', views.generation, name='Text'),
    path('translate/', views.translate, name='Translation'),

]