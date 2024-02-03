from django.test import TestCase
from django.urls import reverse
from restaurant_app.models import Items,Reservation,Membership
from restaurant_app.forms import ItemsForm,ReservationForm,MembershipForm

class ItemViewsTest(TestCase):
    def setUp(self):
        self.item = Items.objects.create(
            name = '',
            description = 'This is only for test',
            type = 'food',
            price = 3.5
        )
        self.item_data = {
            'name': 'drink',
            'description': 'this is only for test',
            'type': 'food',
            'price': 3.5
        }


    def test_intro_page_view(self):
        response = self.client.get(reverse('intro_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')
        self.assertContains(response,'food')
        self.assertContains(response,'This is only for test')