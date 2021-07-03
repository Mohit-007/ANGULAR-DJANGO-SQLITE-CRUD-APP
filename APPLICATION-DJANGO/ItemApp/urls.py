from django.conf.urls import url
from ItemApp import views

urlpatterns = [
    url(r'^items/$', views.itemApi),     
    url(r'^item/([0-9]+)$', views.itemApi)   

]

