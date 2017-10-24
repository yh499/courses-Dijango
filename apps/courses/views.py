from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages



def index(request):
    context = {
        'courses': Course.objects.all()
    }
    context['info'] = Course.objects.all()
    return render(request, 'courses/index.html', context)

def create(request):
    print request
    name = request.POST['name']
    des = request.POST['des']
    y = {'name': name, 'des': des}
    errors = Course.objects.basic_validator(y)
    if errors:
        for tag, error in errors.itervalues():
            messages.error(request, error, extra= tag)    
    else:
        Course.objects.create(name = name, des = des)
        return redirect('/')
    print request.POST['des']

def delete(request, course_id):
    courseobj = Course.objects.get(id=course_id)
    return render(request, 'courses/destroy.html',{'course': courseobj} )


def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')