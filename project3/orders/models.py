from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Review (models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} - {self.rating} out of 5 - {self.review}'


class Topping (models.Model):
    topping = models.CharField(max_length = 30)

    def __str__ (self):
        return f'{self.topping}'

class Pizza (models.Model):
    SMALL = 'S'
    LARGE = 'L'

    SICILIAN = 'SC'
    REGULAR = 'R'

    SIZE = [
    (SMALL, 'Small'),
    (LARGE, 'Large')
    ]

    TYPE = [
    (SICILIAN, 'Sicilian'),
    (REGULAR, 'Regular')
    ]

    type = models.CharField(max_length = 2, choices = TYPE, default = REGULAR)
    size = models.CharField(max_length = 2, choices = SIZE, default = SMALL)
    toppings = models.ManyToManyField(Topping, blank = True)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__ (self):
        if self.toppings.count() == 0:
            return f'{self.type} - {self.size} - ${self.price} - No toppings'
        else:
            return f'{self.type} - {self.size} - ${self.price} - {self.toppings.in_bulk()}'

class SubExtra(models.Model):
    name = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class Sub(models.Model):
    SMALL = 'S'
    LARGE = 'L'

    SIZE = [
    (SMALL, 'Small'),
    (LARGE, 'Large')
    ]

    name = models.CharField(max_length = 40)
    size = models.CharField(max_length = 2, choices = SIZE, default = SMALL)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    extra = models.ManyToManyField(SubExtra, blank = True)


    def __str__(self):

        if self.extra.count() == 0:
            return f'{self.name} - size: {self.size} - ${self.price} with no extras'
        else:
            return f'{self.name} - size: {self.size} - ${self.price} with {self.extra.in_bulk()}'

class Pasta(models.Model):
    name = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class Salad(models.Model):
    name = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class DinnerPlatter(models.Model):
    SMALL = 'S'
    LARGE = 'L'

    SIZE = [
    (SMALL, 'Small'),
    (LARGE, 'Large')
    ]
    name = models.CharField(max_length = 40)
    size = models.CharField(max_length = 2, choices = SIZE, default = SMALL)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f'{self.name} - {self.get_size_display()} - ${self. price}'

class PizzaOrder(Pizza):
    CHOICES = [
        ('CH', 'Cheese'),
        ('1', '1 Topping'),
        ('2', '2 Toppings'),
        ('3', '3 Toppings'),
        ('SP', 'Special')
    ]

    type = Pizza.type
    size = Pizza.size
    extras = models.CharField(max_length=15 ,choices=CHOICES, default='CH')
    toppings = Pizza.toppings
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.get_type_display()} - {self.get_size_display()} - {self.get_extras_display()}"

class Order (models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    pizza = models.ForeignKey (Pizza, blank = True, null = True, on_delete=models.CASCADE)
    sub = models.ForeignKey(Sub, blank = True, null = True, on_delete=models.CASCADE)
    salad = models.ForeignKey(Salad, blank = True, null = True, on_delete=models.CASCADE)
    pasta = models.ForeignKey(Pasta, blank = True, null = True, on_delete=models.CASCADE)
    dinnerplatter = models.ForeignKey(DinnerPlatter, null = True, blank = True, on_delete=models.CASCADE)
    subextra = models.ForeignKey(SubExtra, blank = True, null = True, on_delete=models.CASCADE)
    order_completed = models.BooleanField(default=False)
