from django.db import models

# Create your models here.
 
class User(models.Model):
    username = models.TextField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=100)

    def __str__(self)-> str:
        return self.username
    
