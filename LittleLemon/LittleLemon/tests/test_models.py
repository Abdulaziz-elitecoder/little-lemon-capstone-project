from django.test import TestCase
from restaurant.models import *
from restaurant.views import *


class MenuTest(TestCase):
    def test_get_itew(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemStr = item.__str__()
        self.assertEqual(itemStr, "IceCream : 80")
