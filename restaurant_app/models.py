from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
from datetime import date

bad_words = ['son of a bitch', 'cunt', 'motherfucker', 'cockroach', 'elephant']

def validate_bad_words(value):
    for word in bad_words:
        if word in value:
            raise ValidationError('No bad words allowed.')

def validate_age(value):
    if value:
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18 or age > 100:
            raise ValidationError("Age must be between 18 and 100.")

def validate_email(value):
    if value and value.endswith('.what'):
        raise ValidationError("Email address should not end with '.what'.")
    


class Items(models.Model):
    TYPE_CHOICES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
    ]
    name = models.CharField(max_length=255, unique=True, validators=[validate_bad_words, validators.validate_slug])
    description = models.TextField(blank=True, validators=[validate_bad_words])
    type = models.CharField(max_length= 20,choices =TYPE_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=10)
#choicefield would be food or beverage 'type' then choice Field
    def clean(self):
        pass
    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}"


class Reservation(models.Model):
    first_name = models.CharField(max_length=255, validators=[validate_bad_words])
    last_name = models.CharField(max_length=255, validators=[validate_bad_words])
    email = models.EmailField(validators=[validate_email, validators.EmailValidator(message='Enter a valid email.')])
    time = models.CharField(max_length=255)
    number_of_people = models.IntegerField()
    
    def clean(self):
        if not self.first_name or not self.last_name:
            raise ValidationError("No bad words.")
    
    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.time}"

class Membership(models.Model):
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
#foreign key would delete first_name and last_name under Reservation class.
    def clean(self):
        if not self.first_name or not self.last_name:
            raise ValidationError("No bad words.")
    
    
    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.reason}"


