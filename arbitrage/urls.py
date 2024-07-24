from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.get_all_arbitrages, name='list_all_arbitrages'),
    path("active/", views.get_active_arbitrages, name='list_active_arbitrages'),
    path("inactive/", views.get_inactive_arbitrages, name='list_historical_arbitrages'),
    path("delete/<int:id>/", views.delete_arbitrage, name='delete_arbitrage'),
]
