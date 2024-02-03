from django.urls import path
from .views import homepage,intro_page,second_page,second_detail,third_page,fourth_page,fourth_detail,success_page,information_page,information_detail,shopping_page,membership_page,membership_detail,membership_success

urlpatterns = [
    #path('',homepage,name='home'),
    path('intro/',intro_page,name='intro_page'),
    path('second/',second_page,name='second_page'),
    path('second/<str:name>/',second_detail,name='second_detail'),
    path('third/', third_page, name='third_page'),
    path('fourth/',fourth_page,name='fourth_page'),
    path('fourth_detail/', fourth_detail,name='fourth_detail'),
    path('success_page/',success_page,name='success_page'),
    path('information/', information_page, name='information_page'),
    path('information_detail', information_detail,name='information_detail'),
    path('shopping/',shopping_page,name='shopping_page'),
    path('membership/',membership_page,name='membership_page'),
    path('membership_detail/',membership_detail,name='membership_detail'),
    path('membership_success',membership_success,name='membership_success')

    
]