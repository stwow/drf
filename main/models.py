from django.db import models


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class User(models.Model):
    name = models.CharField(max_length=25)
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE)

    def __str__(self):
        return f'Имя  - {self.name}'


class Material(models.Model):
    A = (
        ('a', 'aaaaaaa'),
        ('b', 'bbbbbb'),
        ('c', 'ccccccc'),
    )
    title = models.ManyToManyField('ProductModel')
    model = models.CharField(max_length=100, choices=A, default='a')
    user = models.OneToOneField('User', on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(max_length=25)
    city = models.ForeignKey('City', on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=25)
    population = models.PositiveIntegerField()

