from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if (request.POST):
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Account created for {username}.")
            return redirect('recipe-home')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form': form})

def profile(request, pkey):
    context = {
        'profile': User.objects.get(pk=pkey).profile
    }
    return render(request, "users/profile.html", context)

@login_required 
def update_profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "users/update_profile.html", context)