from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
	"courses": Course.objects.all()
	}
	return render(request, 'course_review/index.html', context)

def destroy(request, course_id):
	context = {
	"id": (Course.objects.get(id=course_id).id),
	"name": (Course.objects.get(id=course_id).name),
	"desc": (Course.objects.get(id=course_id).desc)
	}
	return render(request, 'course_review/destroy.html', context)

def delete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')

def create(request):
	Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
	return redirect('/')