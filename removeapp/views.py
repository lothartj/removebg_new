from django.shortcuts import render

# Create your views here.
def mainview(request):
    return render(request, 'removeapp/index.html')