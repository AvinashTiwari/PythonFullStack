from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from appTwo import views

urlpatterns = [
    url(r'^$',views.help, name='help'),

]
