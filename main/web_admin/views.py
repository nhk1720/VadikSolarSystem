from django.shortcuts import render

def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def product_view(request):
    return render(request, 'main/product.html')

def video_view(request):
    return render(request, 'main/videos.html')
def address_view(request):
    return render(request, 'main/address.html')