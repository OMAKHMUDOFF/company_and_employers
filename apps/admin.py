from django.contrib import admin
from .models import Company, Employer, Employee, Position

# Register your models here.

admin.site.register(Employee)
admin.site.register(Position)


@admin.register(Company)
class Companies(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Employer)
class Employers(admin.ModelAdmin):
    list_display = ("name", "salary", "company", "position")
    search_fields = ("name", "position", "company")
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")
