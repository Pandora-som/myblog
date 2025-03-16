from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class State(models.Model):
    name_state = models.CharField(max_length=255)
    state_text = models.TextField()
    date_state = models.DateTimeField()
    def __str__(self):
        return self.name_state
    
class Comment(models.Model):
    comment_text = models.TextField()
    date_comment = models.DateTimeField()
    state_id = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.comment_text
    
    