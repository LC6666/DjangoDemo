from django.test import TestCase
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

    def test_display_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1',response.content.decode())
        self.assertIn('itemey 2', response.content.decode())
