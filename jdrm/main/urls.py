from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main),
    # path('users', views.users),
    # path('users', views.audits),
    # path('users', views.events),
]
