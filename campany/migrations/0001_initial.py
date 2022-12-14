# Generated by Django 4.1.3 on 2022-11-07 03:04

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название департамента')),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='campany.departament')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменты',
                'db_table': 'departament',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='Зарплата')),
                ('hire_date', models.DateTimeField(auto_now=True, verbose_name='Дата принятия на работу')),
                ('departament', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='campany.departament', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'db_table': 'employee',
            },
        ),
    ]
