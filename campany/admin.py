from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from campany.models import Employee, Departament
from campany.repositories import DepartamentRepository


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
            "first_name",
            "last_name",
            "patronymic",
            "salary",
            "hire_date",
            "departament",
    )
    list_editable = (
            "departament",
    )
    list_per_page = 50
    list_display_links = ("first_name",)
    sortable_by = list_display
    save_on_top = True


@admin.register(Departament)
class DepartamentAdmin(DjangoMpttAdmin):
    tree_title_field = 'name'
    tree_display = ('name',)
    tree_auto_open = 0
    tree_load_on_demand = 0
    use_context_menu = False
    """
        Момент с tree_auto open
        Надо очищать local storage
        https://github.com/mbraak/django-mptt-admin/issues/256
    """

    def get_queryset(self, request):
        return DepartamentRepository.fetch_all_departaments()

