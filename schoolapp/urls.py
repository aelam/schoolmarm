from django.conf.urls import url
from schoolapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]