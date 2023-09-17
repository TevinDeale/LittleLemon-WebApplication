from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class TestMenuItem(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Vanilla IceCream', price=1.50, inventory=35)
        self.assertEqual(item.title, 'Vanilla IceCream')
        self.assertEqual(item.price, 1.50)