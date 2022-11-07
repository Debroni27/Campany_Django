from django.contrib import admin
from django.core.cache import cache
from django.core.paginator import Paginator
from django_mptt_admin.admin import DjangoMpttAdmin

from campany.models import Employee, Departament


# Оптимизация запроса orm
class CachingPaginator(Paginator):
    def _get_count(self):

        if not hasattr(self, "_count"):
            self._count = None

        if self._count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self._count = cache.get(key, -1)
                if self._count == -1:
                    self._count = super().count
                    cache.set(key, self._count, 3600)

            except:
                self._count = len(self.object_list)
        return self._count

    count = property(_get_count)


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
    list_per_page = 50
    list_display_links = ("first_name",)
    list_select_related = ['departament']
    show_full_result_count = False
    paginator = CachingPaginator


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
    show_full_result_count = False
    paginator = CachingPaginator


