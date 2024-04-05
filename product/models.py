from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6)

    # Обновите определения связей
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="product_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="product_user_set",
        related_query_name="user",
    )


class Category(models.Model):
    name = models.CharField(max_length=200)


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
