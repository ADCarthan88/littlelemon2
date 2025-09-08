from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=50, inventory=50)

        def test_getall(self):
            items = Menu.objects.all()
            serialized_items = MenuSerializer(items, many=True)
            expected_data = serialized_items.data
            self.assertEqual(len(expected_data), 2)
            self.assertEqual(expected_data[0]['title'], "IceCream")
            self.assertEqual(expected_data[1]['title'], "Cake")