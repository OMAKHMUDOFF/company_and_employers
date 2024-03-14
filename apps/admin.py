from django.contrib import admin
from .models import Company, Employer, Employee
# Register your models here.

admin.site.register(Company)
admin.site.register(Employee)

@admin.register(Employer)
class PostAdmin(admin.ModelAdmin):
  list_display = ('name', 'company', 'position', 'salary')
  search_fields = ('name','position')
  list_filter = ("created_at",)
  readonly_fields = ("created_at", 'updated_at')