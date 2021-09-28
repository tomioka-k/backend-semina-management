from django.utils import timezone
from django.db import models
from django.db.models import manager
from django.db.models.enums import Choices
from accounts.models import User


class Seminar(models.Model):

    affiliation_choices = (
        ('防水', '防水'),
        ('床', '床'),
        ('住建', '住建'),
        ('複合', '複合')
    )

    method_choices = (
        ('会場', '会場'),
        ('オンライン', 'オンライン')
    )

    # Basic
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=10, choices=method_choices)
    affiliation = models.CharField(max_length=5, choices=affiliation_choices)
    staff = models.CharField(max_length=50)
    place = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    start_application_date = models.DateField(null=True)
    end_application_date = models.DateField(null=True)
    number_of_attendees = models.IntegerField(default=0)
    capacity = models.IntegerField(null=True)

    application_page = models.URLField(max_length=200, blank=True)
    application_list = models.URLField(max_length=200, blank=True)
    autience_page = models.URLField(max_length=200, blank=True)
    event_page = models.URLField(max_length=200, blank=True)
    is_reserved = models.BooleanField(default=False)

    # Mail
    invitation_mail = models.DateField(null=True)
    remaind_mail = models.DateField(null=True)
    viewing_guide_mail = models.DateField(null=True)
    thank_you_mail = models.DateField(null=True)

    creater = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
