from django.test import TestCase
from lists.models import Item,List

# Create your tests here.

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List.objects.create()

        first_item = Item()
        first_item.text = 'The first(ever) list item'
        first_item.list = list_
        first_item.save()


        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual('The first(ever) list item', first_saved_item.text)
        self.assertEqual('Item the second', second_saved_item.text)