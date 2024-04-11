# charging_locator/urls.py

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the homepage (index.html)
    path('charging-station-map/', views.charging_station_map, name='charging_station_map'),  # URL for charging station map view
    path('carbon-footprint/', views.carbon_footprint_calculator, name='carbon_footprint_calculator'),
    re_path(r'^carbon-footprint/result/(?P<carbon_footprint>[\d.]+)/$', views.carbon_footprint_result, name='carbon_footprint_result'),  # Use re_path with a regular expression
    path('charging-stations/<int:station_id>/', views.charging_station_detail, name='charging_station_detail'),  # URL for charging station detail view
    path('charging-stations/<int:station_id>/review/', views.submit_charging_station_review, name='submit_charging_station_review'),  # URL for submitting a review
    path('community-reviews/', views.community, name='community_reviews'),  # URL for the community reviews page
]
