from django.shortcuts import render
from .forms import HelloForm


def index(request):
    if len(request.GET) != 0:
        form = HelloForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            return render(request, 'index.html', context={'name': name, 'message': message})
    form = HelloForm()
    return render(request, 'index.html', context={'form': form})