"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Service.views import ServiceAPI
from Service import views as view

urlpatterns = [
    path('api/services/', ServiceAPI.as_view(), name='service_api'),
    path('initial/',view.initial),
    path('composition/', view.composition),
    path('addNewService/',view.add_new_service),
    path('getAllService/',view.get_all_service)
]
