from django.shortcuts import render

def Login(request):

    return render(request, 'task-tracker/login.html')

def SignUp(request):
    
    return render(request, 'task-tracker/signup.html')