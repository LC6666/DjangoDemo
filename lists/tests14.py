# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from django.test import TestCase
from lists.views import Item

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new',data={'item_text':'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new',data={'item_text':'A new list item'})
        self.assertRedirects(response,'/lists/the-only-list-in-the-world/')