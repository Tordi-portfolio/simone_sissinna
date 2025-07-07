from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.caption[:30]}"


from django.db import models

class FansCard(models.Model):
    name = models.CharField(max_length=200)
    card_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField()
    image = models.ImageField(upload_to='fanscards/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.card_type}"



from django.db import models
from django.contrib.auth.models import User

# Unique FanCard Product Model (What users can buy)
class StoreFanCard(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fancards/store/')
    card_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Unique Purchased FanCard Belonging to Users
class UserFanCardRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    store_card = models.ForeignKey(StoreFanCard, on_delete=models.SET_NULL, null=True, blank=True)
    card_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    # Admin uploaded image for this user's fans card
    delivered_card_image = models.ImageField(upload_to='fancards/delivered/', blank=True, null=True)
    message = models.TextField(blank=True, help_text="Optional message or details from admin.")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Fan Card"
        verbose_name_plural = "User Fan Cards"

    def __str__(self):
        return f"{self.user.username} - {self.store_card.name if self.store_card else 'Card'}"
