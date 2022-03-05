from django.conf.urls import url
from django.urls import path
from .views import (ExcusesView, )


app_name = 'webapp'

urlpatterns = [
    path('excuses/<str:func>', ExcusesView.as_view()),
]