from django.urls import path
from anime_videos.views import *


urlpatterns = [
    path('', main_view, name='home'),
    path('<int:id>/', video_view, name='video'),
    path('genre/<str:genre>/', genre_view, name='genre'),
    path('feedback/', feedback_view, name='feedback'),
    path('top100/', top100_view, name='top100'),
]
