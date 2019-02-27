from django.shortcuts import render, HttpResponse, redirect
from .models import Resim
from .forms import PostForm
from PIL import Image

# Create your views here.
def index(request):
    resimler = Resim.objects.all()
    return render(request, 'index.html', {'resimler': resimler})

def resimEkle(request):
    #if request.method == "GET":
    #    return redirect('/')
    #else:
    #    title = request.POST.get('title')
    #    newImg = Resim(title = title)

    #    newImg.save()
    #    return redirect('/')

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('/')