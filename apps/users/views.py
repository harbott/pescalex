#/apps/users/
from django.http import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from pescalex.apps.users.models import UserProfile
from pescalex.apps.users.forms import LoginForm, RegisterForm, RecoverForm, ProfileForm

import datetime

def users_login(request, error=False):
    """ Check if the user is a valid django auth user and log him to the system. """
    message = False
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']            
           
            # try to login the user.
            user = authenticate(email=username, password=password)
            
            if user is not None:
                if user.is_active:
                    # success
                    django_login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    # account is not active
                    message = 'Your account is not active.'
            else:
                # wrong user/ pass combination
                message = 'Sorry that login was not recognised'
                #return HttpResponseRedirect(reverse('user_failed_login', args=['failed']))
        else:
            message = 'Please enter both your email address and password'
            
    return render_to_response('users/login.html', {'form':form, 'message':message}, context_instance=RequestContext(request))

def users_recover(request):
    form = RecoverForm()
    message = False
    
    if request.method == 'POST':
        form = RecoverForm(request.POST)
        
        if form.is_valid():
            message = 'A new password has been emailed to you.'

    return render_to_response('users/recover.html', locals(), context_instance=RequestContext(request))

def users_register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            # try to register new user.
            user = form.save(commit=False)
            user.username = form.cleaned_data['email'][:30]
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            return HttpResponseRedirect(reverse('users_login'))
            
    return render_to_response('users/register.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def users_profile(request):
    user = UserProfile.objects.get(id=request.user.id)
    form = ProfileForm(instance=user)
    message = False
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)

        if form.is_valid():
            if form.cleaned_data['password'] == '':
                form.password = user.password
            else:
                user.set_password(form.cleaned_data['password'])
                
            form.save()
            form = ProfileForm(instance=user)
            
            message = 'Your Profile has been saved.'
            
    return render_to_response('users/profile.html', locals(), context_instance=RequestContext(request))