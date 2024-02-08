from django.urls import path

from . import views

urlpatterns = [
    path('api', views.testar_api),
    path('bancos', views.testar_bancos)
]