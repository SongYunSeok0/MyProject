from django import forms
from sh_shop.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['type', 'gender', 'brand', 'price', 'size', 'content', 'uploaded_image']
        widgets = {
            'price': forms.TextInput(attrs={
                'id': 'id_price',
                'placeholder': '가격을 입력하세요',
                'autocomplete': 'off',
            })
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if isinstance(price, str):
            price = price.replace(',', '')
        try:
            return int(price)
        except (ValueError, TypeError):
            raise forms.ValidationError("숫자만 입력하세요.")
