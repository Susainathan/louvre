from django.db import models


class Registeron(models.Model):
    Name=models.CharField(max_length=30)
    Email = models.EmailField()
    Age=models.IntegerField()
    gen=(
        ("Male","Male"),
        ("Female","Female")
    )
    Gender=models.CharField(max_length=10, choices=gen)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class Ticket(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Age = models.IntegerField()
    gen = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    Gender = models.CharField(max_length=10, choices=gen)
    Date=models.DateField()
    Tickets=models.IntegerField()
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)