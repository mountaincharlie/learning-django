from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    # context => data that needs to be used in the rendered template
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)  # returns a HttpResponse


def add_item(request):
    # the POST handler
    if request.method == 'POST':
        # getting the info from the form
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # calling the function to return to home
            return redirect('get_todo_list')
    # using forms.py
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)  # returns a HttpResponse


def edit_item(request, item_id):
    # getting the item from the db
    item = get_object_or_404(Item, id=item_id)
    # the POST handler
    if request.method == 'POST':
        # getting the info from the form
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # specifying the data the form should be pre-popped with
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done  # switching its done status
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()  # deleting the item
    return redirect('get_todo_list')
