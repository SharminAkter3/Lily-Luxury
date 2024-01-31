from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"