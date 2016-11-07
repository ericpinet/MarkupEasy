from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.projects_dashboard, name='projects_dashboard'),
]