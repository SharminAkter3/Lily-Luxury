from django.db import models
from flower.models import Flower
from account.models import User

# Create your models here.

ORDER_STATUS = [("Completed", "Completed"), ("Pending", "Pending")]


class Order(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=ORDER_STATUS, max_length=20, default="Pending")
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Flower : {self.flower.title}, User: {self.user.username}"
