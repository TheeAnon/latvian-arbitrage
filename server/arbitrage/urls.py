from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_arbitrages, name='list_arbitrages'),
    path("post-arbitrage/", views.post_arbitrage, name='post_arbitrages'),
]
