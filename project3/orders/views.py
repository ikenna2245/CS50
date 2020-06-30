from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review, Topping, Pizza, SubExtra, Sub, Pasta, Salad, DinnerPlatter, PizzaOrder, Order
from django.utils import timezone

# Create your views here.
def index(request):
    review = Review.objects.all()
    if request.method == 'POST':
        if Review.objects.filter(author=request.user):
            messages.warning(request, f'A review has previously been submitted by you')
        else:
            rating = request.POST.get('range')
            review = request.POST.get('textarea')
            reviews = Review(author = request.user, rating = rating, review = review, date=timezone.now())
            reviews.save()
            messages.success(request, f'review has been submitted successfully')
            return redirect ('index')
    return render(request, "orders/index.html", {'review': review})

def menu(request):
    context = {
            "toppings": Topping.objects.all(),
            "pizzas": Pizza.objects.all(),
            "subs": Sub.objects.all(),
            "subextras": SubExtra.objects.all(),
            "pastas": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "dinnerplatters": DinnerPlatter.objects.all(),
            "order": Order.objects.filter(user=request.user, order_completed = False)
        }
    return render(request, 'orders/menu.html', context)

@login_required
def subs(request):
    if request.method == 'POST':
        order = request.POST.get('sub')
        sub = Sub.objects.get(pk=order)
        newOrder = Order(user= request.user, sub = sub)
        newOrder.save()
        return redirect ('menu')
    else:
        return redirect('menu')

@login_required
def salad(request):
    if request.method == 'POST':
        order = request.POST.get('salad')
        salad = Salad.objects.get(pk=order)
        newOrder = Order(user= request.user, salad = salad)
        newOrder.save()
        return redirect ('menu')
    else:
        return redirect('menu')

@login_required
def pasta(request):
    if request.method == 'POST':
        order = request.POST.get('pasta')
        pasta = Pasta.objects.get(pk=order)
        newOrder = Order(user= request.user, pasta = pasta)
        newOrder.save()
        return redirect ('menu')
    else:
        return redirect ('menu')

@login_required
def dinnerplatter(request):
    if request.method == 'POST':
        order = request.POST.get('platter')
        platter = DinnerPlatter.objects.get(pk=order)
        newOrder = Order(user= request.user, dinnerplatter = platter)
        newOrder.save()
        return redirect ('menu')
    else:
        return redirect ('menu')

@login_required
def extra(request):
    if request.method == 'POST':
        order = request.POST.get('extra')
        extra = SubExtra.objects.get(pk=order)
        newOrder = Order(user= request.user, subextra = extra)
        newOrder.save()
        return redirect ('menu')
