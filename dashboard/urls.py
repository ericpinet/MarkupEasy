from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^([-\w.]+)/$', views.user_dashboard, name='dashboard'),
    url(r'^([-\w.]+)/([0-9]+)/$', views.project, name='project'),

]
