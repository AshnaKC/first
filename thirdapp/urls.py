"""third_project URL Configuration

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
from thirdapp.views import home,add_product,edit_product,show_product,register,login_page,logout_fn,delete,edit_user,change_password


urlpatterns = [
    path('home/',home, name='home'),
    path('product/',add_product,name='add_product'),
    path('edit/<int:id>/',edit_product,name='edit_product'),
    path('category/<int:id>/',show_product,name='show_product'),
    path('register/',register,name='register'),
    path('login/',login_page,name='login'),
    path('logout/',logout_fn,name='logout'),
    path('delete/<int:id>',delete,name='delete'),
    path('edit/user',edit_user,name='edit_user'),
    path('password/',change_password,name='change_password')


]
