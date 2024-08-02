from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView
from todoApp2.forms import UserRegisterForm,UserLoginForm,TodoForm,TodoUpdateForm
from django.contrib.auth.models import User
from todoApp2.models import TodoModel
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.
class Home(TemplateView):
  template_name='App2/index.html'

class UserTegisterView(CreateView):
  template_name='App2/user_register.html'
  form_class=UserRegisterForm
  model=User
  success_url=reverse_lazy('homeView')

  def form_valid(self, form):
    fname=form.cleaned_data.get("first_name")
    lname=form.cleaned_data.get('last_name')
    uname=form.cleaned_data.get('username')
    email=form.cleaned_data.get('email')
    psw=form.cleaned_data.get('password')
    User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=psw)
    messages.success(self.request,'Registration Success!')
    return redirect('homeView')

class UserLogin(View):
  def get(self,request):
    form=UserLoginForm()
    return render(request,'App2/user_login.html',{'form':form})
  def post(self,request):
    uname=request.POST.get('username')
    psw=request.POST.get('password')
    user=authenticate(request,username=uname,password=psw)
    if user:
      login(request,user)
      messages.success(request,"App2/Login Successful \n welcom")
      return redirect('homeView')
    else:
      messages.error(request,'Invalid credentials')
      return redirect('logView')

class TodoCreateView(CreateView):
  template_name='App2/add_todo.html'
  form_class=TodoForm
  model=TodoModel
  success_url=reverse_lazy('homeView')

  def form_valid(self, form):
    form.instance.user=self.request.user
    messages.success(self.request,'Todo create Success')
    return super().form_valid(form)

class TodoListView(ListView):
  template_name='App2/list_todo.html'
  model=TodoModel
  context_object_name='todo'

  def get_queryset(self):
    return TodoModel.objects.filter(user=self.request.user)

class TodoDetailView(DeleteView):
  template_name='App2/todo_detail.html'
  model=TodoModel
  context_object_name='todo'
  pk_url_kwarg='id'  #if you give 'pk' in html page insted of 'id' then you dond need this line

class TodoUpdateView(UpdateView):
  template_name='App2/todo_update.html'
  model=TodoModel
  form_class=TodoUpdateForm
  success_url=reverse_lazy('listView')
  pk_url_kwarg='id'

  def form_valid(self,form):
    messages.success(self.request,'Updated')
    return super().form_valid(form)

class TodoDeleteView(DeleteView):
  model=TodoModel
  pk_url_kwarg='id'
  success_url=reverse_lazy('listView')
  template_name='App2/delete_view.html'