from django.shortcuts import render, HttpResponse, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'default/index.html', context)

def add(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'default/destroy.html', context)

def delete(request, id):
    if request.POST['submit'] == "No":
        pass
    elif request.POST['submit'] == "Yes! I want to delete this":
        Course.objects.get(id=id).delete()
    return redirect('/')
