# Generated by Django 4.1 on 2022-11-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personalExpenses', '0009_delete_user_delete_userexpense'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='userExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField(max_length=10, null=True)),
                ('month', models.TextField(default='January', max_length=12)),
                ('expense', models.PositiveIntegerField(default=None)),
                ('income', models.PositiveIntegerField(default=None)),
                ('saving', models.PositiveIntegerField(default=None)),
            ],
        ),
    ]
