from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from extendedUser.models import NewUser
import os
# Create your models here.


class TourPicture(models.Model):
    
    image = models.ImageField(upload_to='tour_images/')    

class Tour(models.Model):
    PACKAGE_CHOICE=[
        ('Basic', 'Basic'),
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
    ]

    title = models.CharField(max_length=100)
    destination = models.CharField(max_length=100,null=True, blank=True)
    short_desc = models.CharField(max_length=100,null=True, blank=True )
    desc = models.CharField(max_length=500 ,null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True) 
    start_date = models.DateField((""), auto_now=False, auto_now_add=False, blank=True)
    end_date = models.DateField((""), auto_now=False, auto_now_add=False, blank=True)
    package_type=models.CharField(max_length=50,choices=PACKAGE_CHOICE,null=True, blank=True)
    agent=models.ForeignKey(NewUser, verbose_name=("Agent Name"), on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    tour_pictures = models.ManyToManyField('TourPicture', blank=True, related_name='tours')


    def clean(self):
        if self.agent and not self.agent.groups.filter(name='Agent').exists():
            raise ValidationError("The selected agent must belong to the 'Agent' group.")
    
    def end_date_validation(self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be greater than start date.")
    
    class Meta:
        verbose_name = ("Tour")
        verbose_name_plural = ("Tour's")

    def __str__(self):
        return f"{self.title} "

    def get_absolute_url(self):
        return reverse("tour_details", kwargs={"pk": self.pk})
