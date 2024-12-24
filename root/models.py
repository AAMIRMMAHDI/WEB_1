from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    scheduled = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="test")
    name_servise = models.CharField(max_length=100, default="Default Service ")  
    about_content = models.TextField(default="test")
    image = models.ImageField(upload_to='services', default='services.jpg')
    Edelectus_content_name = models.TextField(default="test")
    Edelectus_content_Description = models.TextField(default="test")
    Temporibus_content_name = models.TextField(default="test")
    Temporibus_content_Description = models.TextField(default="test")
    Feature_content = models.TextField(default="test")
    Description_content_name = models.TextField(default="test")
    Description_content_Description = models.TextField(default="test")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)


class Resume(models.Model):
    name0 = models.CharField(max_length=100, default="test")
    name1 = models.CharField(max_length=100, default="test")
    name2 = models.CharField(max_length=100, default="test")
    name3 = models.CharField(max_length=100, default="test")
    name4 = models.CharField(max_length=100, default="test")
    name5 = models.CharField(max_length=100, default="test")
    scheduled = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="test")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ('created_at',)


class About(models.Model):
    name11 = models.CharField(max_length=100, default="test")
    name12 = models.CharField(max_length=100, default="test")
    name0 = models.CharField(max_length=100, default="test")
    name1 = models.CharField(max_length=100, default="test")
    name2 = models.CharField(max_length=100, default="test")
    name3 = models.CharField(max_length=100, default="test")
    name4 = models.CharField(max_length=100, default="test")
    name5 = models.CharField(max_length=100, default="test")
    name6 = models.CharField(max_length=100, default="test")
    name7 = models.CharField(max_length=100, default="test")
    name8 = models.CharField(max_length=100, default="test")
    name9 = models.CharField(max_length=100, default="test")
    name10 = models.CharField(max_length=100, default="test")
    scheduled = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="test")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name0
    
    class Meta:
        ordering = ('created_at',)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.user.username
