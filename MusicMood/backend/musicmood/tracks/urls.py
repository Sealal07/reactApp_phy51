from django.urls import path
from .views import TracksListView, TimeOfDayView

urlpatterns = [
    path('tracks/', TracksListView.as_view(),
         name='track-list'),
    path('tracks/mood/', TimeOfDayView.as_view(),
         name='time-of-day-tracks'),
]