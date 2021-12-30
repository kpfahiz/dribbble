from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User =get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Category(models.Model):
    title = models.CharField(max_length=20)


    def __str__(self)->str:
        return self.title

class Post(models.Model):
    title =models.CharField(max_length=100)
    overview = models.TextField()
    #slug = models.SlugField(unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self)->str:
        return self.title
    
    def get_absalute_url(self):
        return reverse('post_details',kwargs={
            'id':self.id,
        })
    def get_update_url(self):
        return reverse('post_update',kwargs={
            'id':self.id,
        })
    def get_delete_url(self):
        return reverse('post_delete',kwargs={
            'id':self.id,
        })
