from django.urls import path
from todoApp2 import views

urlpatterns=[
  path('todo/home',views.Home.as_view(),name='homeView'),
  path('todo/login',views.UserLogin.as_view(),name='logView'),
  path('todo/register',views.UserTegisterView.as_view(),name='regView'),
  path('todo/add',views.TodoCreateView.as_view(),name='addView'),
  path('todo/list',views.TodoListView.as_view(),name='listView'),
  path('todo/data/<int:id>',views.TodoDetailView.as_view(),name='dataView'),
  path('todo/update/<int:id>',views.TodoUpdateView.as_view(),name='updateView'),
  path('todo/delete/<int:id>',views.TodoDeleteView.as_view(),name='deleteView'),
]
