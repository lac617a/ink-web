from django.shortcuts import render

# Create your views here.

def windowMain(request):
    return render(request,'home.html')