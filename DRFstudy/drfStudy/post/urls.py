"""
URL configuration for drfStudy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from post.views import PostView, PostCreateAPIView, PostDetailView, PostUserListAPIView, PostListAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDestroyAPIView

urlpatterns = [
    path('apiview/', PostView.as_view()),
    path('apiview/<int:pk>', PostDetailView.as_view()),

    path('generics/create', PostCreateAPIView.as_view()),
    path('generics/list', PostListAPIView.as_view()),
    path('generics/<int:pk>', PostRetrieveAPIView.as_view()),
    path('generics/<int:pk>/update', PostUpdateAPIView.as_view()),
    path('generics/<int:pk>/destroy', PostDestroyAPIView.as_view()),

]
