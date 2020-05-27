from django.shortcuts import render,redirect
from .models import Image,Category,Location
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def home(request):

    return render(request,'searches/home.html')

def music(request):
    wrap = {
        'images':Image.objects.all()
    }
    

    return render(request,'searches/image.html',wrap)

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'searches/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searches/search.html',{"message":message})

def search_location(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'searches/location.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searches/search.html',{"message":message})        
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"searches/single.html", {"image":image})    

def images(request,image_location): 
    try:
        image = Image.objects.get(location = image_location)
    except DoesNotExist:
        raise Http404()
    return render(request,"searches/single.html", {"image":image})    


def tropics(request):
    images = Image.objects.filter(id =2) and Image.objects.filter(id =3)
 
    wrap = {
      'images':images

    }
    return render(request,'searches/tropics.html',wrap)


