from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NeighbourHoodForm, PostForm, BusinessForm
from .models import Neighbourhood, Business, Post



def index(request):
    mitaa_zote = Neighbourhood.objects.all()
    return render(request, 'neighbourhood/index.html', {'mitaa_zote':mitaa_zote})


def add_mtaa(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            mtaa = form.save(commit=False)
            mtaa.admin = request.user.profile
            mtaa.save()
            return redirect('add_mtaa')
    else:
        form = NeighbourHoodForm()
    return render(request, 'create_mtaa.html', {'form': form})

@login_required(login_url='login')
def mitaa(request):
    mitaa_zote = Neighbourhood.objects.all()
    mitaa_zote = mitaa_zote[::-1]
    params = {
        'mitaa_zote': mitaa_zote,
    }
    return render(request, 'mitaa_zote.html', params)


def create_post(request, mtaa_id):
    mtaa = Neighbourhood.objects.get(id=mtaa_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.mtaa = mtaa
            post.user = request.user
            post.save()
            return redirect('mtaa', mtaa.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})



def mtaa(request, mtaa_id):
    mtaa = Neighbourhood.objects.get(id=mtaa_id)
    business = Business.objects.filter(id=mtaa_id)
    posts = Post.objects.filter(id=mtaa_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = mtaa
            b_form.user = request.user
            b_form.save()
            return redirect('mtaa', mtaa.id)
    else:
        form = BusinessForm()

    
    params = {
        'mtaa': mtaa,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'mtaa.html', params)



