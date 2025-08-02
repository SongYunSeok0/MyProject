from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
   
class Post(models.Model):
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)
    content=models.CharField(null=True)
    uploaded_image = models.ImageField(upload_to='images/',
                                       blank=True)
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return f'{self.name}----{self.slug}'
    def get_url(self):
        return f'/category/{self.slug}'