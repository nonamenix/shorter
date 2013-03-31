from django.contrib import admin
from core.models import Short


class ShortAdmin(admin.ModelAdmin):
    list_display = ('short_urn','full_uri','created_at','conversions')
admin.site.register(Short, ShortAdmin)