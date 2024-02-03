from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Items,Reservation
from django.contrib.auth.models import User
from .forms import ReservationForm,MembershipForm
#def functions 
def homepage(request):
    return HttpResponse('<h1>Hi Welcome!</h1>')

def intro_page(request):
    return render(request,'restaurant_app/intro_list.html')

def second_page(request):
    items = Items.objects.all()
    return render(request,'restaurant_app/second_page.html',{'items':items})

def second_detail(request,name):
    item = get_object_or_404(Items, name=name)
    return render(request, 'restaurant_app/second_detail.html', {'item':item})
def third_page(request):
    return render(request, 'restaurant_app/third_page')


def fourth_page(request):
   return render(request, 'restaurant_app/fourth_page.html')
    

def fourth_detail(request):
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            
            # Create and save a new Reservation instance to the database
            form.save()
            print(form)
            return redirect('success_page')
    else:
        form = ReservationForm()

    return render(request, 'restaurant_app/fourth_page.html', {'form': form})



def success_page(request):
    return render(request, 'restaurant_app/success_page.html')

def information_page(request):
    return render(request, 'restaurant_app/information_page.html')

def information_detail(request):
    return render(request, 'restaurant_app/information_detail.html')

def shopping_page(request):
    return render(request,'restaurant_app/shopping_page.html')

def membership_page(request):
    return render(request,'restaurant_app/membership_page.html')

def membership_detail(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            
            # Create and save a new Reservation instance to the database
            form.save()
            print(form)
            return redirect('membership_success')
    else:
        form = MembershipForm()

    return render(request, 'restaurant_app/membership_page.html', {'form': form})



def membership_success(request):
    return render(request, 'restaurant_app/membership_success.html')

