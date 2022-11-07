from django.views.generic import ListView

from campany.repositories import DepartamentRepository


class DepartamentListView(ListView):
    """Отображаем список всех подразделений"""
    context_object_name = "departament"
    template_name = 'campany/base.html'
    queryset = DepartamentRepository.fetch_all_departaments()
