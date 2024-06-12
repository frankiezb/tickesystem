from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'USERS/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    # Redirect to the home page after login


# Define the signup view as a standalone function
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page you want
    else:
        form = UserCreationForm()
    return render(request, 'USERS/signup.html', {'form': form})


    


