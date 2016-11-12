from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^save_personal_information$', views.save_personal_information, name='save_personal_information'),
]
