from django.contrib import admin
from .models import Order
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render, redirect

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "flower_name",
        "user_name",
        "quantity",
        "status",
        "cancel",
    ]

    def flower_name(self, obj):
        return obj.flower.title

    def user_name(self, obj):
        return obj.user.username

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.status == "Completed":
            email_subject = "Your Order is Confirmed"
            email_body = render_to_string(
                "admin_email.html",
                {"user": obj.user, "flower": obj.flower},
            )

            email = EmailMultiAlternatives(email_subject, "", to=[obj.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()


admin.site.register(Order, OrderAdmin)
