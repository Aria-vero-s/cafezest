from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from django.utils import timezone


GUESTS = (
    ("1 guest", "1 guest"),
    ("2 guests", "2 guests"),
    ("3 guests", "3 guests"),
    ("4 guests", "4 guests"),
    ("5 guests", "5 guests"),
    ("6 guests", "6 guests"),
    ("7 guests", "7 guests"),
    ("8 guests", "8 guests"),
    )
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
    ("9 PM", "9 PM"),
)


class Booking(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    guests = models.CharField(max_length=50, choices=GUESTS, default="1 guest", blank=False, null=False)
    First_name = models.CharField(max_length=50, help_text='First name', blank=False, null=False)
    Last_name = models.CharField(max_length=50, help_text='Last name', blank=False, null=False)
    Email = models.EmailField(max_length=100, help_text='Email', blank=False, null=False)
    Phone = models.CharField(max_length=20, help_text='Phone', blank=False, null=False)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, blank=False, null=False)
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    date_ordered = models.DateField(default=datetime.now)

    def __str__(self):
        return f"day: {self.day} | time: {self.time}"

