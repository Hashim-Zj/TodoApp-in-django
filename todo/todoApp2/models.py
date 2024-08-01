from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
  title=models.CharField(max_length=100)
  content=models.CharField(max_length=700)
  date=models.DateField(auto_now_add=True)
  status=models.BooleanField(default=False) 
  user=models.ForeignKey(User,on_delete=models.CASCADE)
