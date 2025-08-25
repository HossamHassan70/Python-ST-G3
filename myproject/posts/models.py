from django.db import models

# Create your models here.
# post (#id, title, description, image, date)
# Models Benefits (db size, Html widget, validation) 
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title
    
class User(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    
    def __str__(self):
        return self.first_name