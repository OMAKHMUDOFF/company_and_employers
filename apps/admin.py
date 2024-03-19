from django.contrib import admin
from .models import Company, Employer, Employee, Position

# Register your models here.

admin.site.register(Position)


@admin.register(Company)
class Companies(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Employer)
class Employers(admin.ModelAdmin):
    list_display = ("name", "received_salary", "company", "position", "him_employees")
    search_fields = ("name", "company", "position")
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Employee)
class Employees(admin.ModelAdmin):
    list_display = (
        "name",
        "salary",
        "company",
        "position",
        "employer",
    )
    search_fields = ("name", "company", "position")
    list_filter = ("created_at",)
    readonly_fields = ("created_at", "updated_at")
