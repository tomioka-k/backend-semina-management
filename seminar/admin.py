from django.contrib import admin
from django.db.models import fields
import import_export
from .models import Seminar
from import_export import resources
from import_export.admin import ImportExportMixin
# Register your models here.


class SeminarResources(resources.ModelResource):
    class Meta:
        model = Seminar
        fields = '__all__'


@admin.register(Seminar)
class SeminarAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = Seminar
        resources = SeminarResources
