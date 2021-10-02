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
    name = models.CharField(verbose_name="セミナー名", max_length=255)
    method = models.CharField(
        verbose_name="開催方法", max_length=10, choices=method_choices)
    affiliation = models.CharField(
        "所属", max_length=5, choices=affiliation_choices)
    department = models.CharField(verbose_name="部署", max_length=50)
    staff = models.CharField(
        verbose_name="担当者", max_length=50, blank=True, null=True)
    place = models.CharField("場所", max_length=255, blank=True, null=True)
    start_date = models.DateField(verbose_name="開催日")
    end_date = models.DateField(verbose_name="終了日")
    start_application_date = models.DateField(
        verbose_name="申込開始日", blank=True, null=True)
    end_application_date = models.DateField(
        verbose_name="申込締切日", blank=True, null=True)
    number_of_attendees = models.IntegerField(verbose_name="出席者", default=0)
    capacity = models.IntegerField(verbose_name="定員", blank=True, null=True)

    application_page = models.URLField(
        verbose_name="申込ページ", max_length=200, blank=True, null=True)
    application_list = models.URLField(
        verbose_name="申込者一覧", max_length=200, blank=True, null=True)
    audience_page = models.URLField(
        verbose_name="視聴ページ", max_length=200, blank=True, null=True)
    event_page = models.URLField(
        verbose_name="イベントページ", max_length=200, blank=True, null=True)
    is_reserved = models.BooleanField(verbose_name="ZOOM予約", default=False)

    # Mail
    invitation_mail = models.DateField(
        verbose_name="招待メール配信日", blank=True, null=True)
    remaind_mail = models.DateField(
        verbose_name="リマインドメール配信日", blank=True, null=True)
    viewing_guide_mail = models.DateField(
        verbose_name="視聴案内メール配信日", blank=True, null=True)
    thank_you_mail = models.DateField(
        verbose_name="御礼メール配信日", blank=True, null=True)

    creater = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name="作成日", auto_now=True)
    updated_at = models.DateTimeField(verbose_name="更新日", auto_now_add=True)

    def __str__(self):
        return self.name
