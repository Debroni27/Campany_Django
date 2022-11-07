import datetime

from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Departament(MPTTModel):
    """модель департамента (вложенное дерево, количество 5)"""
    name = models.CharField(max_length=64, unique=True, verbose_name="Название департамента")
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, db_index=True)
    slug = models.SlugField(max_length=30, blank=True)

    class Meta:
        unique_together = [['parent', 'slug']]
        db_table = 'departament'
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    """модель работника"""
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    salary = models.IntegerField(blank=True, null=True, verbose_name='Зарплата')
    hire_date = models.DateTimeField(auto_now=datetime.datetime.now(), verbose_name="Дата принятия на работу")
    departament = TreeForeignKey('Departament', on_delete=models.PROTECT, related_name="employee_departament", verbose_name='Департамент')
    class Meta:
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'Работник: {self.last_name} {self.first_name}'

