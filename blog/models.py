from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class BlogPost(models.Model):
    name = models.CharField(max_length=200, help_text='Give it a name')
    description = models.TextField(max_length=1000)
    author = models.ForeignKey('BlogAuthor', on_delete=models.CASCADE)
    post_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['-post_date']
    
class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, help_text='Tell me about you')
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('blog-author-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['user__username']

class BlogComment(models.Model):
    description = models.TextField(max_length=500)
    post_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
    @admin.display(description = 'Blog Comment')
    def truncate_str(self):
        str = self.description
        if (len(str) > 75):
            str = str[:75] + ' ...'    
        return str
    
    class Meta:
        ordering = ['post_date']
    