from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Client


def signin(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            action = request.POST.get('action', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)

            if action == 'signin':
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('/')
    context = {}
    return render(request, 'signin/signin.html', context)

def signup(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		if request.method == 'POST':
			action = request.POST.get('action', None)
			email = request.POST.get('email', None)
			password = request.POST.get('password', None)
			name = request.POST.get('name', None)

			if action == 'signup':
				client = Client.objects.create_user(email=email,
	                                            password=password,
	                                            name=name,)
				client.save()
				return redirect('/signin')
	context = {}
	return render(request, 'signin/signup.html', context)
