from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title=models.TextField(max_length=200,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    forget_password_token=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
