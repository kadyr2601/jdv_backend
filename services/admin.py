from django.contrib import admin
from services.models import Service, Maintenance


class MaintenanceInline(admin.StackedInline):
    model = Maintenance
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [MaintenanceInline, ]