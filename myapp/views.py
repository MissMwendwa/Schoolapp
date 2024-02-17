from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        user = authenticate(
            request, username = request.POST['username'], password =request.POST['password'])
        if user is None:
            message.error(
                request, 'username and Password did not Match. Please Try again')
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect('homepage')
    else:
        return render(request, 'login.html')