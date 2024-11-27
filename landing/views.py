from django.shortcuts import render, redirect
from .models import Item
from .forms import AddItem, SimpleForm

from django.contrib.auth.decorators import login_required

@login_required
def landing_view(request):
    all_food_data = Item.objects.all()
    return render(request, "landing/home.html", context={'all_foods': all_food_data})

def detail_view(request, id):
    item = Item.objects.get(pk=id)
    return render(request, "landing/detail.html", context={'item':item})

@login_required
def add_item(request):
    form = SimpleForm(request.POST or None)
    if form.is_valid():
        new_item = Item.objects.create(
            item_name = form.cleaned_data['name'],
            item_desc = form.cleaned_data['desc'],
            item_price = form.cleaned_data['price'],
            item_img = form.cleaned_data['image_url'],
            item_author = request.user.username
        )
        new_item.save()
        return redirect('landing:index')
    return render(request, "landing/form.html", context={"form": form})

def edit_item(request, id):
    item = Item.objects.get(pk=id)
    form = SimpleForm(request.POST or None, initial={
        "name":item.item_name,
        "desc":item.item_desc,
        "price":item.item_price,
        "image_url":item.item_img
    })
    if form.is_valid():
        item.item_name = form.cleaned_data['name']
        item.item_desc = form.cleaned_data['desc']
        item.item_price = form.cleaned_data['price']
        item.item_img = form.cleaned_data['image_url']
        item.save()
        return redirect('landing:index')
    return render(request, "landing/form.html", context={"form": form})

def delete_view(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('landing:index')
    return render(request, 'landing/delete.html', context={'name': item.item_name})
