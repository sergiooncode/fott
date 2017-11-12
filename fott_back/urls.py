from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coordinates/', views.index, name='index'),
]
