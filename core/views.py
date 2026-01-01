from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def noticias(request):
    return render(request, 'noticias/feed.html', {
        'noticias': Noticia.objects.order_by('-creado')
    })

@login_required
def crear_noticia(request):
    form = NoticiaForm(request.POST or None)
    if form.is_valid():
        n = form.save(commit=False)
        n.autor = request.user
        n.save()
        return redirect('/noticias/')
    return render(request, 'noticias/crear.html', {'form': form})

@login_required
def recuerdos(request):
    return render(request, 'recuerdos/lista.html', {
        'recuerdos': Recuerdo.objects.order_by('-creado')
    })

@login_required
def crear_recuerdo(request):
    form = RecuerdoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        r = form.save(commit=False)
        r.autor = request.user
        r.save()
        return redirect('/recuerdos/')
    return render(request, 'recuerdos/crear.html', {'form': form})

@login_required
def resenas(request):
    return render(request, 'resenas/lista.html', {
        'resenas': Resena.objects.select_related('item')
    })

@login_required
def crear_resena(request):
    form = ResenaForm(request.POST or None)
    if form.is_valid():
        item, _ = ItemResenable.objects.get_or_create(
            nombre=form.cleaned_data['nombre'],
            categoria=form.cleaned_data['categoria']
        )
        Resena.objects.create(
            autor=request.user,
            item=item,
            puntaje=form.cleaned_data['puntaje'],
            comentario=form.cleaned_data['comentario']
        )
        return redirect('/resenas/')
    return render(request, 'resenas/crear.html', {'form': form})
