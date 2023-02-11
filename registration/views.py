from django.views import generic
from .forms import RegisterForm, UserLoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout , authenticate, login
from django.shortcuts import render, redirect


# Create your views here.


# class UserRegisterView(generic.CreateView):
#     form_class = RegisterForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

def UserRegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('login')
        else:
            form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def UserLoginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')

            else:
                return redirect('login')
            #     # Return an 'invalid login' error message.
        else:
            return render(request, 'registration/login.html', {})



def Logout_view(request):
    logout(request)
    return redirect('home')