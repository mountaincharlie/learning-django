from django.test import TestCase  # used in python's unittest
from .models import Item  # for creating an example item to test

# Create your tests here.


class TestViews(TestCase):

    def test_get_todo_list(self):
        # using builtin HTTP client to get HTTP responses of the views
        response = self.client.get('/')  # for home page
        self.assertEqual(response.status_code, 200)  # the 'ok' response
        self.assertTemplateUsed(response, 'todo/todo_list.html') # temp check


    def test_get_add_item_pg(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_edit_item_pg(self):
        # need to create an example item to test item_id functionality
        item = Item.objects.create(name='Test Todo Items')
        response = self.client.get(f'/edit/{item.id}')  # get request
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        # making up a new item to add
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # if correct redirect => adding was successful
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        # creating an item to test deleting
        item = Item.objects.create(name='Test Todo Items')
        response = self.client.get(f'/delete/{item.id}')  # get request
        # if correct redirect => adding was successful
        self.assertRedirects(response, '/')
        # checking its not possible to get it anymore
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Items', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
