from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
        path('', views.secrets),
        path('facebook/', views.face),
        path('error/', views.data),
        ]






urlpatterns += staticfiles_urlpatterns()
