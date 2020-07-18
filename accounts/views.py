from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # delete the session after signup
            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')

    form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
