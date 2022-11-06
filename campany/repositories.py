
from django.db.models import Prefetch

from campany.models import Departament, Employee

class DepartamentRepository:
    """
        Подготовка кастомного querysetа для модели Departament
    """

    @staticmethod
    def fetch_all_departaments():
        return Departament.objects.prefetch_related(
            Prefetch(
                "employee_departament",
                Employee.objects.filter(departament__in=[1, 2])
            )
        )
