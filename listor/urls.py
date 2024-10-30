from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.AllaListor.as_view(), name='lista-hem'),
    path('lista/<int:pk>/', views.EnLista.as_view(), name='lista-sida'),
    path('lista/<int:pk>/uppdatera', views.UppdateraLista.as_view(), name='lista-uppdatera'),
    path('lista/<int:pk>/radera', views.RaderaLista.as_view(), name='lista-radera'),
    path('lista/ny', views.NyLista.as_view(), name='lista-ny'),
    path('lista/<int:pk>/dela', views.SharedListCreateView.as_view(), name='lista-dela'),

    path('vara/<int:pk>/uppdatera', views.UppdateraVara.as_view(), name='vara-uppdatera'),
    path('vara/<int:pk>/radera', views.RaderaVara.as_view(), name='vara-radera'),
    path('vara/<int:pk>/ny', views.NyVara.as_view(), name='vara-ny'),
    path('rensa/<int:pk>/', views.RensaVaror.as_view(), name='vara-rensa'),

    path('registrera/', views.registrera, name='registrera'),
    path('loggain/', auth_views.LoginView.as_view(template_name='listor/loggain.html'), name='loggain'),
    path('loggaut/', auth_views.LogoutView.as_view(), name='loggaut'),
]
