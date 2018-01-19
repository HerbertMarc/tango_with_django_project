
from django.conf.urls import url
from FistApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
]
