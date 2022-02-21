from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'a.html')
def cos(request):
    return render(request,'b.html')
def con(request):
    return render(request,'c.html')
