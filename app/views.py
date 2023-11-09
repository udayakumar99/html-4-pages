from django.shortcuts import render

# Create your views here.
def name(request):
    return render(request,'name.html')
def two(request):
    return render(request,'two.html')
def three(request):
    return render(request,'three.html')
def four(request):
    return render(request,'four.html')

