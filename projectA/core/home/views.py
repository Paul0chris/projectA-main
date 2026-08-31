from django.shortcuts import render

# Create your views here.
def homeP(request):
    return render(request, "home.html")