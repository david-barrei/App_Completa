from django.contrib import admin
from .models import *
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=['nom','ap','am','area','estado']
    search_fields = 'nom','ap','am'
    list_filter = ['area','estudios']
    list_per_page =5

admin.site.register(Personal, PersonAdmin)
admin.site.register(Area)
admin.site.register(Estudios)