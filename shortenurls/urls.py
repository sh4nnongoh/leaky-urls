from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shorten/<str:encoded_url>', views.shorten, name="shorten"),
    path('<str:shorten_url>/details',
         views.shorten_details, name="shorten-details"),
    path('<str:shorten_url>',
         views.redirect_shorten_url, name="redirect-shorten-url"),
]
