from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name


class Flower(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="flower/images/")
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


STAR_CHOICES = [
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
]

# STAR_CHOICES = [
#     ("1", "⭐"),
#     ("2", "⭐⭐"),
#     ("3", "⭐⭐⭐"),
#     ("4", "⭐⭐⭐⭐"),
#     ("5", "⭐⭐⭐⭐⭐"),
# ]


class Review(models.Model):
    reviwer = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name="reviews")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"Reviewer: {self.reviwer.username}; Flower: {self.flower.title}"
