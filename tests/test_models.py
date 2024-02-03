from django.test import TestCase
from restaurant_app.models import Items,Reservation,Membership
from datetime import date
from django.utils import timezone
from django.core.exceptions import ValidationError


class ItemsModelTest(TestCase):
    def setUp(self):
        self.item_data = {
            'name': 'testname',
            'description': 'This is a test description',
            'price': 3.5
        
        }
    def tearDown(self):
        Items.objects.all().delete()
    
    def test_name_creation(self):
        item = Items.objects.create(**self.item_data)
        self.assertEqual(item.name,'testname')
        self.assertEqual(item.description, 'This is a test description')
        self.assertEqual(item.price, 3.5)
    
    def test_name_validation_bad_words(self):
        with self.assertRaises(ValidationError):
            Items.objects.create(name='son of a bitch',description='motherfucker', price=3.5)


class ReservationModelTest(TestCase):
    def setUp(self):
        self.reservation_data ={
            'first_name': 'niyar',
            'last_name': 'gaz',
            'email': 'hexagon@gmail.com',
            'time': '14:00',
            'number_of_people': 6
        }
    
    def tearDown(self):
        Reservation.objects.all().delete()
    
    def test_reservation_creation(self):
        reservation = Reservation.objects.create(**self.reservation_data)
        self.assertEqual(reservation.first_name,'niyar')
        self.assertEqual(reservation.last_name,'gaz')
        self.assertEqual(reservation.email,'hexagon@gmail.com')
        self.assertEqual(reservation.time,'14:00')
        self.assertEqual(reservation.number_of_people, 6)
    
    def test_reservation_validation_bad_words(self):
        with self.assertRaises(ValidationError):
            Reservation.objects.create(first_name='cunt', last_name='elephant', email='hexagon@gmail.com',time='14:00',number_of_people=6)
    
    def test_reservation_validation_email(self):
        with self.assertRaises(ValidationError):
            Reservation.objects.create(first_name='niyar', last_name='gaz',email='alberthuge@.what', time='14:00',number_of_people=6)


class MembershipModelTest(TestCase):
    def setUp(self):
        self.membership_data = {
            'first_name': 'Juan',
            'last_name': 'Horowitz',
            'email': 'juanhoro23@gmail.com',
            'date_of_birth': '1987-08-23',
            'reason':'I want to meet new people'
        }
    
    def tearDown(self):
        Membership.objects.all().delete()
    
    def test_membership_creation(self):
        membership = Membership.objects.create(**self.membership_data)
        self.assertEqual(membership.first_name,'Juan')
        self.assertEqual(membership.last_name,'Horowitz')
        self.assertEqual(membership.email,'juanhoro23@gmail.com')
        self.assertEqual(membership.date_of_birth, date(1987,8,23))
        self.assertEqual(membership.reason,'I want to meet new people')

    def test_membership_validation_bad_words(self):
        with self.assertRaises(ValidationError):
            Membership.objects.create(first_name='cunt', last_name='elephant', email='juanhoro23@gmail.com',date_of_birth='1987-08-23',reason='I want to meet new people')
    
    
    def test_membership_validate_age(self):
        with self.assertRaises(ValidationError):
            Membership.objects.create(first_name='Juan',last_name='Horowitz',email='juanhoro23@gmail.com',date_of_birth=date.today(),reason='I want to meet new people')
        with self.assertRaises(ValidationError):
            Membership.objects.create(first_name='Juan',last_name='Horowitz',email='juanhoro23@gmail.com',date_of_birth=date(1900,1,1),reason='I want to meet new people')
