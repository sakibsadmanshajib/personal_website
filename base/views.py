from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib import messages

def user_login(request):
    context = {}
    next = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('finance_management:account')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')
    
    else:
        return render(request, 'auth/login.html', context)


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('base:login')
