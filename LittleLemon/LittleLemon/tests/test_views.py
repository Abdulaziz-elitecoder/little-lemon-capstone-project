from django.test import TestCase, RequestFactory
from restaurant.models import *
from restaurant.views import *


class MenuViewTest(TestCase):
    def setUp(self):
        menu_item = Menu.objects.create(title="Coffee", price=80, inventory=100)
        return super().setUp()
        
    def test_getall(self):
        request = RequestFactory().get('/restaurant/menu/')
        view = MenuItemsView()
        view.setup(request)

        context = str(view.get_queryset())
        self.assertIn('Coffee : 80.00', context)