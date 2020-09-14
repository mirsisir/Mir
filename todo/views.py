from django.shortcuts import render,redirect
from .models import task
from .forms import taskForm
from django.contrib import messages

# Create your views here.
def index(request):
    all_task = task.objects.all
    count= task.objects.all().count()
    
    
    if request.method == 'POST':
        form = taskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_task = task.objects.all
            
            messages.success(request,('new task added'))
    
            return render(request,'home.html',{'all_task' : all_task , 'count': count})


    
    return render(request,'home.html',{'all_task' : all_task , 'count': count})

def delete(request,task_id):
    item = task.objects.get(pk=task_id)
    item.delete()
    return redirect('index')


def marking(request, task_id):

    item = task.objects.get(pk=task_id)
    if item.completed == False:
        item.completed = True
        item.save()
    else:
        item.completed = False
        item.save()
    return redirect('index')


def update(request, task_id):
	tas = task.objects.get(pk=task_id)

	form = taskForm(instance=tas)

	if request.method == 'POST':
		form = taskForm(request.POST, instance=tas)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'update.html', context)

def today(request):
    all_task= task.objects.filter(catagory="Today's Task")
    count= task.objects.filter(catagory="Today's Task").count()
    print(today)

    return render(request,'home.html',{'all_task' : all_task , 'count': count})






