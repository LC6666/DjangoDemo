from django.test import TestCase
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')