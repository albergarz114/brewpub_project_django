#class methods 
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from django.http import HttpResponse
from .models import Items,Reservation, Membership
from django.urls import reverse_lazy
from .forms import ItemsForm, ReservationForm, MembershipForm
import logging
logger = logging.getLogger(__name__)



#class IntroPageView(TemplateView):
#    template_name = 'restaurant_app/intro_list.html'
    

