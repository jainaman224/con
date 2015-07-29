from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Task
def index(request):
	a=Task.objects.all()
	context={'polls':a}
	return render(request,'polls/task.html',context)

def purchase(request):
    a=Task.objects.all()
    context={'polls':a}
    return render(request,'polls/purchase.html',context)


