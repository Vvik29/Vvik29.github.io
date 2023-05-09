from django import forms
from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm
from .models import Feedback, Message
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.models import User



class UserCreatForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')



class UpdateProfileForm(forms.ModelForm):
    #username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email')
        fields = ('first_name', 'last_name', 'email')




class PasswordChangeForm(DjangoPasswordChangeForm):
    pass


class UserInfoForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': ' ',
            'first_name': ' ',
            'last_name': ' ',
            'email': ' ',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': ' '}),
            'first_name': forms.TextInput(attrs={'placeholder': ' '}),
            'last_name': forms.EmailInput(attrs={'placeholder': ' '}),
            'email': forms.TextInput(attrs={'placeholder': ' '}),
        }

        label_suffix = ''



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
