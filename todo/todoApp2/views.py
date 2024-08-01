from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,CreateView
from todoApp2.forms import UserRegisterForm,UserLoginForm,TodoForm
from django.contrib.auth.models import User
from todoApp2.models import TodoModel
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.
class Home(TemplateView):
  template_name='index.html'

class UserTegisterView(CreateView):
  template_name='user_register.html'
  form_class=UserRegisterForm
  model=User
  success_url=reverse_lazy('home_veiw')

  def form_valid(self, form):
    fname=form.cleaned_data.get("first_name")
    lname=form.cleaned_data.get('last_name')
    uname=form.cleaned_data.get('username')
    email=form.cleaned_data.get('email')
    psw=form.cleaned_data.get('password')
    User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=psw)
    messages.success(self.request,'Registration Success!')
    return redirect('home_veiw')

class UserLogin(View):
  def get(self,request):
    form=UserLoginForm()
    return render(request,'user_login.html',{'form':form})
  def post(self,request):
    uname=request.POST.get('username')
    psw=request.POST.get('password')
    user=authenticate(request,username=uname,password=psw)
    if user:
      login(request,user)
      messages.success(request,"Login Successful \n welcom")
      return redirect('home_veiw')
    else:
      messages.error(request,'Invalid credentials')
      return redirect('user_login')

class TodoCreateView(CreateView):
  template_name='add_todo.html'
  form_class=TodoForm
  model=TodoModel
  success_url=reverse_lazy('home_view')

  def form_valid(self, form):
    form.instance.user=self.request.user
    messages.success(self.request,'Todo create Success')
    return super().form_valid(form)