from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from campany.models import Employee, Departament


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name",)}


@admin.register(Departament)
class DepartamentAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}

