"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from education import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('dialog/<int:id>/', views.get_dialog),
    path('sett', views.add_dialog),
    path('dial', views.get_all_dialogs),
    path('chatbot', views.chatbot),
    path('search/<str:searchstring>', views.search),
    path('result', views.result),
    path('card/<str:path>', views.card_detail),
    path('form', views.form),
    path('createuser', views.form_add_user),
]
