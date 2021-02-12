"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # ()       endpoint    func         nameAssigned
#     #!        |           |            |
#     #!        v           v            v
#     path('', views.index, name='index'),
#     path('input/', views.inputs, name='input'),
#     path('removePunc/', views.removePunc, name='removePunc/'),
#     path('capitalizeFirst/', views.capFirst, name='capFirst'),

#     path('newLineRemover/', views.newLineRemover, name='newLineRemover'),
#     path('spaceRemover/', views.spaceRemover, name='spaceRemover'),
#     path('charCount/', views.charCount, name='charCount'),


# ]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('about', views.about, name='about')
]
