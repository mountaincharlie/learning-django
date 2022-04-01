from django.test import TestCase  # used in python's unittest
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):  # inheriting the TestCase class

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})  # this empty form should fail
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Tets todo item'})  # testing with any name and no done status
        self.assertTrue(form.is_valid())


    def test_fields_only_used_from_form_meta_class(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
