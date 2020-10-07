"""chatApp URL Configuration

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
from django.urls import path
from chat import views  

urlpatterns = [
        #URL from: "/api/messages/1/2"
        path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  #For GET request.
        #URL from: "/api/messages/"
        path('api/messages/', views.message_list, name='message-list'),  #For POST
        #URL from "/api/users/1"
        path('api/users/<int:pk>', views.user_list, name='user-detail'),  #GET request for user with id
        path('api/users/', views.user_list, name='user-list'),            #POST for new user and GET for all users list. 
]
