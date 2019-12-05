from django.shortcuts import *
from .models import *

# Create your views here.
def home(request):
    return render(request,"app/create.html")

def register(request):
    f=request.POST['fname']
    l=request.POST['lname']
    m=request.POST['mail']
    all_user= lol.objects.create(firstname=f,lastname=l,email=m)
    return HttpResponseRedirect(reverse('show'))

def showid(request):
    user = lol.objects.all()
    return render(request,"app/show.html",{'key':user})

def edit(request):
    n = request.POST['i']
    one_user = lol.objects.filter(id=n)
    return render(request,"app/edit.html",{'key1':one_user})

def change(request):
    c1 = True
    c2 = True
    c3 = True
    f = request.POST['fa']
    l = request.POST['la']
    m = request.POST['ma']
    i = request.POST['id']

    n = lol.objects.get(id=i)
    
    if(f==""):
        c1  = False
    if(l==""):
        c2  = False
    if(m==""):
        c3  = False

    if(c1 == True):
        n.firstname = f
        n.save()
    if(c2 == True):
        n.lastname = l
        n.save()
    if(c3 == True):
        n.email = m
        n.save()
    
    allu = lol.objects.all()

    return render(request,"app/done.html",{'key2':allu})

def del_user(request):
    n = request.POST['g']
    one_user = lol.objects.get(id=n)
    one_user.delete()
    aa = lol.objects.all()
    return render(request,"app/show.html",{'key':aa})