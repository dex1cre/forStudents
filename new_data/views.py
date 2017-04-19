from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    if request.method == "POST":
        html = request.POST['html']
        return render(request, 'new_data/index.html', {'html': html})
    else:
        return render(request, 'new_data/index.html', {'html': '<h1>Hello</h1>'})
