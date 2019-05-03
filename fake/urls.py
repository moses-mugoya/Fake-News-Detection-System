from django.urls import re_path
from . import views

app_name = 'fake'

urlpatterns = [
    re_path('^$', views.fakenews, name='fake')
]
