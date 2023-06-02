from django.shortcuts import render
from .models import Tavarlar

# Create your views here.
def home(request):
    data=Tavarlar.objects.all()
    context={"tavarlar":data}
    return render(request,"home.html",context)