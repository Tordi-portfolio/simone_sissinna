from django.db import models
from django.contrib.auth.models import User

class FanCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fan_cards')

    fan_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    address = models.TextField()
    membership = models.CharField(max_length=50, choices=[
        ('Platinum Fan', 'Platinum Fan'),
        ('Gold Fan', 'Gold Fan'),
        ('Silver Fan', 'Silver Fan'),
        ('Bronze Fan', 'Bronze Fan'),
        ('Vip Fan', 'Vip Fan'),
    ])
    valid_till = models.DateField()
    issued_on = models.DateField(auto_now_add=True)

    fan_photo = models.ImageField(upload_to='fan_cards/photos/')
    keanu_photo = models.ImageField(upload_to='fan_cards/keanu/', default='default_keanu.jpg')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.fan_code}"
