from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User

def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Save to database
            User.objects.create(username=username, email=email, password=password)

            # return render(request, 'success.html') 
            return redirect('success')  # Redirects to a named URL
 # Option 1: directly render the success template
 # Option 2: redirect to a URL pattern named 'success'
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})