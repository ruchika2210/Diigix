# userauth/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
#     profile_picture = forms.ImageField(required=False, label='Profile Picture
# ')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'profile_picture')



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    
    



    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']











        

    # def clean_username(self):
    #     username=self.cleaned_data.get('username')

    #     if User.objects.filter(username=username).exists():
    #         raise ValidationError('username is existing ')

    #     if not username.isalnum():
    #         raise ValidationError('Username can only contain letters and numbers')
        
    #     return username

    # def clean_password1(self):
    #     password1=self.cleaned_data.get('password1')

    #     if len(password1)<8:
    #         raise ValidationError('Password must be atleast 8 characters')
        
    #     if not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1) or not any(char.isalnum() for char in password1):
    #         raise ValidationError('Password must contain at least one digit, one letter, and one special character.')
        
    #     return password1
    

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2=self.cleaned_data.get('password2')

    #     if len(password2)<8:
    #         raise ValidationError('Password must be atleast 8 characters')
        
    #     if not any(char.isdigit() for char in password2) or not any(char.isalpha() for char in password2) or not any(char.isalnum() for char in password2):
    #         raise ValidationError('Password must contain at least one digit, one letter, and one special character.')
        
    #     if password1 and password2 and password1!=password2:
    #         raise ValidationError('Passwords do not match')
        
    #     return password2
        

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError('This email already exists')
    #     return email
                
            
