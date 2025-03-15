from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    
class State(models.Model):
    name_state = models.CharField(max_length=255)
    state_text = models.TextField()
    date_state = models.DateTimeField()
    
class Comment(models.Model):
    name_comment = models.CharField(max_length=255)
    comment_text = models.TextField()
    date_comment = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    
    