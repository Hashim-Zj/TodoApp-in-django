from django.urls import path
from todoApp2 import views

urlpatterns=[
  path('home',views.Home.as_view(),name='home_veiw'),
  path('log',views.UserLogin.as_view(),name='log_view'),
  path('reg',views.UserTegisterView.as_view(),name='reg_veiw'),
  path('addtodo',views.TodoCreateView.as_view(),name='addtodo'),
]
