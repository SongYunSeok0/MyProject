from django import forms
from sh_shop.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['type', 'brand', 'price', 'size', 'content', 'uploaded_image']