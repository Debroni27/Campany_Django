
from django.views.generic import ListView

from campany.services import fetch_all_employees, fetch_all_departments
from campany.models import Departament, Employee


class DepartamentListView(ListView):
    """Отображаем список всех департаментов"""
    model = Departament
    template_name = 'campany/depart_list.html'


class EmployeeByDepartment(ListView):
    """
        Отображает список работников
        конткертного департамента
    """

    context_object_name = 'employees'
    template_name = 'campany/empl_list.html'

    def get_queryset(self):
        self.departament = Departament.objects.get(slug=self.kwargs['slug'])
        queryset = Employee.objects.filter(departament=self.departament)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.departament
        return context
