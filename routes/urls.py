from django.urls import path

from . import views

urlpatterns = [
  # path for route home page
  path('', views.HomeView.as_view(), name='home'),

  # paths for CRUD relating to Line
  path('lines/', views.LinesView.as_view(), name='lines'),
  path('lines/new/', views.CreateLineView.as_view(), name='create_line'),
  path('lines/<pk>/update/', views.UpdateLineView.as_view(), name='update_line'),
  path('lines/<pk>/delete/', views.DeleteLineView.as_view(), name='delete_line'),

  # paths for CRUD relating to Station
  path('stations/', views.StationView.as_view(), name='stations'),
  path('stations/new/', views.CreateStationView.as_view(), name='create_station'),
  path('stations/<pk>/update', views.UpdateStationView.as_view(), name='update_station'),
  path('stations/<pk>/delete/', views.DeleteStationView.as_view(), name='delete_station'),
  # paths for CRUD relating to Stops
  path('stops/', views.StopView.as_view(), name='stops'),
  path('stops/new/', views.CreateStopView.as_view(), name='create_stop'),
  path('stops/<pk>/update/', views.UpdateStopView.as_view(), name='update_stop'),
  path('stops/<pk>/delete/', views.DeleteStopView.as_view(), name='delete_stop'),

]


