from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
   
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return f'{self.name}----{self.slug}'
    def get_url(self):
        return f'/category/{self.slug}'
    
class Post(models.Model):
    type_CHOICES = [
        ('top', '상의'),
        ('bottom', '하의'),
        ('outer', '아우터'),
        ('shoes', '신발'),
        ('etc', '잡화'),
    ]

    GENDER_CHOICES = [
        ('male', '남성'),
        ('female', '여성'),
        ('unisex', '공용'),
    ]

    type = models.CharField(max_length=20, choices=type_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unisex')

    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)
    content = models.TextField(null=True, blank=True)
    uploaded_image = models.ImageField(upload_to='images/',
                                       blank=True)
    
