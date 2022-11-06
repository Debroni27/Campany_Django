from django.views.generic import ListView
from campany.repositories import DepartamentRepository


class DepartamentListView(ListView):
    """Отображаем список всех подразделений"""
    context_object_name = "departament"
    template_name = 'campany/base.html'
    queryset = DepartamentRepository.fetch_all_departaments()
    paginate_by = 30


# class EmployeeByDepartment(ListView):
#     """
#         Отображает список работников
#         конткертного подразделения
#     """
#     context_object_name = 'employees'
#     template_name = 'campany/depart_list.html'
#     paginate_by = 50
#     def get_queryset(self):
#         return EmployeeRepository.fetch_all_employee()
