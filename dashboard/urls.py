from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^projects-empty$', views.dashboard, name='projects-empty'),
    url(r'^([0-9]+)/$', views.project_details, name='project-details'),

]
