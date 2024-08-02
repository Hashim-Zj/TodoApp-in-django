"""
URL configuration for todo project.

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
from django.urls import path,include
from todo_app import views

urlpatterns = [
    path('',include('todoApp2.urls')),
    path('admin/', admin.site.urls),
    path('h', views.HomeView.as_view(),name='home_view'),
    path('signup', views.UserRegister.as_view(),name='user_reg'),
    path('login', views.UserLogin.as_view(),name='user_login'),
    path('logout', views.UserLogOut.as_view(),name='user_logout'),
    path('addtodo', views.AddTodo.as_view(),name='add_todo'),
    path('listtodo', views.ListTodo.as_view(),name='list_todo'),
    path('detail/<int:id>', views.TodoDetailView.as_view(),name='todo_detail'),
    path('update/<int:id>', views.UpdateTodoView.as_view(),name='todo_update'),
    path('delete/<int:id>', views.DeleteTodoView.as_view(),name='todo_delete'),

]
