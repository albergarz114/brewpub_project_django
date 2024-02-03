from django.test import TestCase
from restaurant_app.models import Items,Beverage,Reservation,Membership
from restaurant_app.forms import ItemsForm,BeverageForm,ReservationForm,MembershipForm

class ItemsFormTest(TestCase):
    def test_valid_item_form(self):
        form_data = {
            'name': 'testname',
            'description': 'This is a test description',
            'price': 3.5
        }
        form = ItemsForm(data=form_data)

    def test_invalid_item_form_bad_words(self):
        form_data = {
            'name': 'cunt',
            'description': 'elephant',
            'price': 3.5
        }
        form = ItemsForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description',form.errors)

class ReservationFormTest(TestCase):
    def test_valid_reservation_form(self):
        form_data = {
            'first_name': 'Manuela',
            'last_name': 'Feldstein',
            'email': 'manlaf@yahoo.com',
            'time': '12:30',
            'number_of_people': 7
        }
        form=ReservationForm(data=form_data)
        

    def test_invalid_reservation_form(self):
        form_data = {
            'first_name': 'cockroach',
            'last_name': 'cunt',
            'email': 'manlaf@yahoo.what',
            'time': '12:30',
            'number_of_people': 7

        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email',form.errors)
        self.assertIn('first_name',form.errors)
        self.assertIn('last_name',form.errors)

class MembershipFormTest(TestCase):
    def test_valid_membership_form(self):
        form_data = {
            'first_name': 'niyar',
            'last_name': 'gaz',
            'email': 'hexagon@gmail.com',
            'time': '14:00',
            'number_of_people': 6
        }
        form=MembershipForm(data=form_data)

    def test_invalid_membership_form(self):
        form_data = {
            'first_name': 'motherfucker',
            'last_name': 'elephant',
            'email': 'hexagon@gmail.what',
            'time': '14:00',
            'number_of_people': 6
        }   
        form = MembershipForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name',form.errors)
        self.assertIn('last_name',form.errors)
        self.assertIn('email',form.errors) 