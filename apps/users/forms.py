#/apps/users/
from django import forms
from django.contrib.admin.models import User
from django.forms.widgets import PasswordInput, HiddenInput
from django.forms import ModelForm
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from pescalex.apps.users.models import UserProfile
from pescalex.settings import DOMAIN_NAME
import random

class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(max_length=15, widget=PasswordInput())
    
class RegisterForm(ModelForm):    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=15, widget=PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.id = kwargs['instance'].id
        else:
            self.id = False
    
    def clean_email(self):
        try:
            email = self.cleaned_data['email']
            if (self.id):
                User.objects.exclude(id=self.id).get(Q(email=email) | Q(username=email))
            else:
                User.objects.get(Q(email=email) | Q(username=email))
            # here we raise error since it seems that we found an entry...?
            raise forms.ValidationError('That email address (' + email + ') is already registered please try another one.')
        except User.DoesNotExist:
            return email

class RecoverForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        data = self.cleaned_data['email']
       
        try:
            user = UserProfile.objects.get(email=data)
            
            # Create temp password
            temp_password = User.objects.make_random_password()
            user.set_password(temp_password)
            user.save()
            
            # Send recover email
            subject = 'Password Recover Request'
            message = render_to_string('users/password_reset_email.txt',
                                       { 'domain': DOMAIN_NAME,
                                         'password': temp_password
                                       }
            )

            print message
            user.email_user(subject, message)
            
        except UserProfile.DoesNotExist:
            raise forms.ValidationError("Sorry we do not recognise that email address.")    
           
class ProfileForm(RegisterForm):  
    password = forms.CharField(max_length=15, required=False, label='Password')
    
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email')
        #exclude = ('password',)