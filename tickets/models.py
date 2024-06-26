from django.db import models


class PostPriority(models.IntegerChoices):
    Urgent = 1
    High = 2
    Medium = 3
    Low = 4

# create your models
class Post(models.Model):
    title = models.CharField(max_length=200)
    priority = models.IntegerField(choices=PostPriority, null=True, blank=True)
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)