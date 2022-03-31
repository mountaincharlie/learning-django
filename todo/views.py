from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)  # returns a HttpResponse


def add_item(request):
    if request.method == 'POST':
        # getting the info from the form
        name = request.POST.get('item_name')
        done = 'done' in request.POST  # checking if its been ticked
        Item.objects.create(name=name, done=done)  # creating the new item
        return redirect('get_todo_list')  # calling the function to return to home

    return render(request, 'todo/add_item.html')  # returns a HttpResponse
