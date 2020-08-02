from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def portfolio_view(request):
    return render(request, 'portfolio.html')


def price_view(request):
    return render(request, 'price.html')


def services_view(request):
    return render(request, 'services.html')


def contact_view(request):
    return render(request, 'contact.html')
