
from django.urls import path

from campany.views import DepartamentListView, EmployeeByDepartment

app_name = "campany"

urlpatterns = [
    path('', DepartamentListView.as_view(), name='departament-list'),
    path('<str:slug>/', EmployeeByDepartment.as_view(), name='employee')
]
