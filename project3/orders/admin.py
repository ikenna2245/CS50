from django.contrib import admin
from .models import Topping, Pizza, SubExtra, Sub, Pasta, Salad, DinnerPlatter, PizzaOrder, Review, Order

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(SubExtra)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(PizzaOrder)
admin.site.register(Review)
admin.site.register(Order)
