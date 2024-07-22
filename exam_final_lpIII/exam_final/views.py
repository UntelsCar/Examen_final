from django.shortcuts import render

# Create your views here.
def personas(request):
    return render(request, 'personas.html')
