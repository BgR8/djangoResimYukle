from django.shortcuts import render, HttpResponse, redirect
from .models import Resim

# Create your views here.
def index(request):
    resimler = Resim.objects.all()
    return render(request, 'index.html', {'resimler': resimler})

def resimEkle(request):
    if request.method == "GET":
        return redirect('/')
    else:
        title = request.POST.get('title')
        newImg = Resim(title = title)

        newImg.save()
        return redirect('/')