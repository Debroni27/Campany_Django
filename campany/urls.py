from django.conf import settings
from django.urls import path, include

from campany.views import DepartamentListView

app_name = "campany"


urlpatterns = [
    path('', DepartamentListView.as_view(), name='departament-list'),
]

