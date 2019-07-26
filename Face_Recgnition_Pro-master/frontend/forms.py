from django import forms 
from .models import User,Image
  
class UserForm(forms.ModelForm): 
  
    class Meta: 
        model = User 
        fields = ['name', 'email'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = Image 
        fields = ['user_img'] 
        widgets = {
            'user_img': forms.FileInput(attrs={'class': 'form-control','multiple':True,'required':True}),
        }