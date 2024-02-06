from django.shortcuts import render
from app1.models import Place,Team
# Create your views here.
def home(request):
    p=Place.objects.all()
    b=Team.objects.all()
    return render(request,"home.html",{'p':p,'b':b})