from django.contrib import admin
from .models import Record
# Register your models here.
@admin.register(Record)
class RecordModel(admin.ModelAdmin):
    pass