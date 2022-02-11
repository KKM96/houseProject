from django.contrib import admin
from .models import Terms


class TermsAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Terms, TermsAdmin)
