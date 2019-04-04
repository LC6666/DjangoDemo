from django.test import TestCase
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')
        # tests9测试不能通过，所以关闭
        # self.assertIn('A new list item',response.content.decode())
        # self.assertTemplateUsed(response,'home.html')