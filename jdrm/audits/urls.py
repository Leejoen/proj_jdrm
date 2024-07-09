from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='page2'),
    path('aud', views.audit, name='audit')
]
