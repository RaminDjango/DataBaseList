from django.shortcuts import render, redirect
from .models import Table
from django.contrib import messages
# Create your views here.


def home(request):
    tabel = Table.objects.all()
    if request.method == 'POST':
        nume    = request.POST['nume']
        prenume = request.POST['prenume']
        email   = request.POST['email']
        card    = request.POST['card']
        if  Table.objects.filter(emails=email).first():
            messages.info(request, 'Ai introdus un email care exista la noi in DataBase')
            return redirect('/')
        else:
            tabel_create = Table.objects.create(name=nume, last_name=prenume, emails=email, cards=card)
            tabel_create.save()    
            return redirect('home')
    context = {
        'tabel':tabel
    }
    return render(request, 'home.html', context)


def edit_item(request, edit_item):
    editare_obiect = Table.objects.get(id = edit_item)
    tabel = Table.objects.all()
    context = {
        'editare_obiect':editare_obiect,
        'tabel':tabel
        
        
    }
    return render(request, 'home.html', context)
    
def update(request, update_item):
    item = Table.objects.get(id = update_item)
    item.name      = request.POST['nume']
    item.last_name = request.POST['prenume']
    item.emails   = request.POST['email']
    item.cards    = request.POST['card']
    item.save()
    messages.info(request, 'Ai EDIT informatile cu success')
    return redirect('home')

def delet(request, delete_item):
    dl = Table.objects.get(id = delete_item)
    dl.delete()
    messages.info(request, 'Ai STERS informatia cu success')
    return redirect('home')

