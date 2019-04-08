from django.test import TestCase
from lists.models import Item,List

# Create your tests here.

class ListViewTest(TestCase):

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1',list=list_)
        Item.objects.create(text='itemey 2',list=list_)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response, 'itemey 2')
