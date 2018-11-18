from django.shortcuts import render

def index(request):
    return render(request, 'main/homepage.html')
def contact(request):
    return render(request, 'main/basic.html')    

# Create your views here.
