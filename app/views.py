from django.shortcuts import render, redirect
from .forms import SignUpForm

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenue')
    else:
        form = SignUpForm()
    return render(request, 'app/form.html', {'form': form})

def bienvenue(request):
    return render(request, 'app/bienvenue.html')