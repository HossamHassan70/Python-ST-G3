from django.db import models

# Create your models here.
# post (#id, title, description, image, date)
# Models Benefits (db size, Html widget, validation) 
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return f'Post: {self.title()}'
    
