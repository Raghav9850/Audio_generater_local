from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_text_to_speech, name='convert_text_to_speech'),
    path('download/', views.download_audio, name='download_audio'),
]