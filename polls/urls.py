from django.urls import path
from . import views

# view.index 로 이동
urlpatterns=[
        path('', views.index, name='index'),
]