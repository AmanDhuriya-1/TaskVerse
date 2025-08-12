from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Consume messages so old ones don't stick around
            list(messages.get_messages(request))
            return redirect('task')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        # Clear old messages on GET requests
        list(messages.get_messages(request))

    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Account created successfully. Please login.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Username already exists')
            except Exception as e:
                messages.error(request, f'Error occurred: {e}')
    return render(request, 'register.html')
