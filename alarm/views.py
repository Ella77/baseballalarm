from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
# Create your views here.
from .forms import playerForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def settings(request):

    if request.method == "POST" :
        form = playerForm(request.POST)

        if form.is_valid():
            player = form.save(commit = False)
            player.user = request.user
            player.save()

        return redirect('wait')
    else :
        form = playerForm()

    return render(request, 'alarm/setting.html', {'form':form})

def main(request):
    return render(request, 'alarm/main.html')

def first(request):
    return render(request, 'alarm/main.html')

def wait(request):
    mydata = player.objects.filter(user=request.user)

    return render(request, 'alarm/wait.html', {'mydata':mydata},)