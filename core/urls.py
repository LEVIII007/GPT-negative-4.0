from django.urls import path, re_path
from . import views
from core.views import index,translate, caption, generation
from . import consumers


urlpatterns = [
    path('', views.index, name='index'),
    path('caption/', views.caption, name='caption'),
    path('generation/', views.generation, name='Text'),
    path('translation/', views.translate, name='Translation'),

]

websocket_urlpatterns = [
    re_path(r'ws/socket-server/$', consumers.captionConsumer.as_asgi()),
]