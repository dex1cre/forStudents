from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    if request.method == "POST":
        number = request.POST['number_task']
        tasks = Tasks.objects.filter(number=number)
        return render(request, 'tasks/subject.html', {'tasks': tasks, 'number': number})
    else:
        return render(request, 'tasks/index.html', {})

def subject(request):
    if request.method == "POST":
        ask = request.POST['ask']
        dd = request.POST['id']
        task = Tasks.objects.get(id=dd)
        if task.ask == ask:
            return HttpResponse('okay')
        else:
            st = "Неверно, правильный ответ: " + task.ask
            return HttpResponse(st)
    else:
        return HttpResponse("ssory, чёт вы не туда зашли)")
    # if request.method == "POST":
    #     form = SubjectForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/admin/subject/new/')
    # else:
    #     form = SubjectForm()
    #     subject = Subjects.objects.all()
    #     return render(request, 'tasks/subject.html', {'form': form, 'subject': subject})
