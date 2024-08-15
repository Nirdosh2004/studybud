from django.shortcuts import render


# Create your views here.

rooms = [
        {'id' : 1, 'name' : 'Lets learn python!'},
        {'id' : 2, 'name' : 'Lets design with me python!'},
        {'id' : 3, 'name' : 'frontend  learn javascript !'},
]

def home(request):
          context =  {'rooms':rooms}
          return render(request, 'base/home.html',context)

def room(request,pk):
        return render(request , 'base/room.html')
