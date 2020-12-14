from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
    if (request.POST):
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if (u_form.is_valid() and p_form.is_valid()):
                u_form.save()
                p_form.save()
                messages.success(request, "Account successfully updated!")
                return redirect(reverse('profile-posts', kwargs={'pkey': request.user.pk}))

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "users/update_profile.html", context)