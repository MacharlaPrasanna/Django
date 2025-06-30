from django.shortcuts import render, HttpResponse
from . models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html',{'tasks':tasks})

def math_operations(request, x , y):
    try:
        result=f"""
        Sum: {x+y} <br>
        Difference: {x-y}<br>
        Product: {x*y}<br>
        Division: {x/y if y !=0 else "not defined"}
        """
    except Exception as e:
        result= f"Error:{str(e)}"
    return HttpResponse(result)

def sum(request,x,y):
    result=x+y
    return HttpResponse(f"Sum of the numbers is {result}")

def difference(request,x,y):
    result=x-y
    return HttpResponse(f"Difference of the numbers is {result}")

def product(request,x,y):
    result=x*y
    return HttpResponse(f"Product of the numbers is {result}")

def division(request,x,y):
    try:
        result=f"""{x/y if y !=0 else "not defined"}"""
    except Exception as e:
        result = f"Error:{str(e)}"
    return HttpResponse(f"Division of the numbers is {result}")