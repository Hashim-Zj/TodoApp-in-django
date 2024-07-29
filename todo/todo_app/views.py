from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm,UserLoginForm,TodoForm,TodoUpdateForm
from django.contrib.auth.models import User
from .models import Todos
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class HomeView(View):
  def get(self,request):
    return render(request,'index.html')

class UserRegister(View):
  def get(self,request):
    form=UserRegisterForm()
    return render(request,'user_register.html',{"form":form})
  def post(self,request):
    form=UserRegisterForm(request.POST)
    if form.is_valid():
      fname=form.cleaned_data.get("first_name")
      lname=form.cleaned_data.get("last_name")
      uname=form.cleaned_data.get("username")
      email=form.cleaned_data.get("email")
      psw=form.cleaned_data.get("password")
      User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=psw)
      messages.success(request,'User Registration Successfully!')
      return redirect('home_view')
    else:
      messages.error(request,"Invalid data")
      return redirect('user_reg')

class UserLogin(View):
  def get(self,request):
    form=UserLoginForm()
    return render(request,'user_login.html',{'form':form})
  def post(self,request):
    # uname=UserLoginForm.cleaned_data.get('username')
    # psw=UserLoginForm.cleaned_data.get('username')
    uname=request.POST.get('username')
    psw=request.POST.get('password')
    user=authenticate(request,username=uname,password=psw)
    if user:
      login(request,user)
      messages.success(request,"Login Successful \n welcom")
      return redirect('home_view')
    else:
      messages.error(request,'Invalid credentials')
      return redirect('user_login')
      
class UserLogOut(View):
  def get(self,request):
    logout(request)
    return redirect('user_login')

class AddTodo(View):
  def get(self,request):
    form=TodoForm()
    return render(request,'add_todo.html',{'form':form})
  def post(self,request):
    if request.user.is_authenticated:
      form=TodoForm(request.POST)
      if form.is_valid():
        title=form.cleaned_data.get('title')
        content=form.cleaned_data.get('content')
        Todos.objects.create(title=title,content=content,user=request.user)
        messages.success(request,'Todo Added success')
        return redirect('list_todo')
      else:
        messages.error(request,'invalid data')
        return redirect("add_todo")
    else:
      messages.warning(request,"you Must login Firs!")
      return redirect("user_login")
    
class ListTodo(View):
  def get(self,request):
    user=request.user
    if user.is_authenticated:
      todo=Todos.objects.filter(user=request.user,status=False)
      return render(request,'list_todo.html',{'todo':todo})
    else:
      messages.warning(request,"You must login First")
      return redirect('user_login')

class TodoDetailView(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get('id')
    todo=Todos.objects.get(id=id)
    return render(request,'todo_detail.html',{'todo':todo})

class DeleteTodoView(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get('id')
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect('list_todo')

class UpdateTodoView(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get('id')
    todo=Todos.objects.get(id=id)
    form=TodoUpdateForm(instance=todo)
    return render(request,'todo_update.html',{'form':form})
  def post(self,request,*args,**kwargs):
      id=kwargs.get('id')
      todo=Todos.objects.get(id=id)
      form=TodoUpdateForm(request.POST,instance=todo)
      if form.is_valid():
        form.save()
        return redirect("list_todo")