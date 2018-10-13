from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
# Create your views here.
from .forms import playerForm


def settings(request):
    if request.method == "POST" :
        form = playerForm(request.POST)

        if form.is_valid():
            player = form.save(commit = False)
            player.user = request.user
            player.save()
        return redirect('main')
    else :
        form = playerForm()

    return render(request, 'alarm/setting.html', {'form':form})

def main(request):
    return render(request,'alarm/main.html')