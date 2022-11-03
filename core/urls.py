
from django.contrib import admin
from django.urls import path, include


from campany.views import DepartamentListView, EmployeeByDepartment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DepartamentListView.as_view(), name='departament-list'),
    path('<str:slug>/', EmployeeByDepartment.as_view(), name='employee-by-departament')
]
