"""scalex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
import views.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result'),
    # path('plans', views.plans, name='plans'),
    # path('statistics', views.statistics, name='statistics'),
    # path('tab', views.tab, name='tab'),
    # path('data', views.data, name='data'),
    # path('export', views.export_data, name='export'),
    path('export_filter_data', views.export_filter_data, name='export_filter_data'),
    # path('admin/', admin.site.urls),
]
