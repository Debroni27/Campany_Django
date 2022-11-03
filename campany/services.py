
from campany.models import Employee, Departament


def fetch_all_employees():
    pass


def fetch_all_departments():
    return Departament.objects.all()
