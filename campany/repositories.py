
from django.db.models import Prefetch
from campany.models import Departament, Employee


class EmployeeRepository:
    @staticmethod
    def fetch_all_employees():
        return Employee.objects.all()


class DepartamentRepository:
    """
        Подготовка кастомного querysetа для модели Departament
    """
    @staticmethod
    def fetch_all_departaments():
        return Departament.objects.prefetch_related(
            Prefetch(
                "employee_departament",
                EmployeeRepository.fetch_all_employees()
            )
        )

