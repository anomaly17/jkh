from django.contrib import admin

from .models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    search_fields = ("account",)
    list_display = ("account", "type", "amount", "is_paid")
    list_filter = ("type", "is_paid")
