from django.test import TestCase  # used in python's unittest
from .models import Item  # importing our model class 'Item'

# Create your tests here.


class TestModels(TestCase):

    def test_done_status_false_as_default(self):
        # creating a new item without specified done status
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)


    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
