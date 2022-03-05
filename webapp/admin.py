from django.contrib import admin
from .models import UserExcuse

# Register your models here.
@admin.register(UserExcuse)
class UserExcuse_tbl(admin.ModelAdmin):
    list_display = ('id', 'user', 'excuse_category', 'excuse', 'excuse_id', 'time_created', 'date_created')
    list_filter = ['user']
    search_fields = ['excuse_category']