from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

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

