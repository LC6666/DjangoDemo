from django.test import TestCase
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

    def test_only_saves_items_when_necessary(self):
        response = self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
