
from django.urls import path

from campany.views import DepartamentListView, EmployeeByDepartment

urlpatterns = [
    path('', DepartamentListView.as_view(), name='departament-list'),
    path('<str:slug>/', EmployeeByDepartment.as_view(), name='employee-by-departament')
]
