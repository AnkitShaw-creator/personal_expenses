# Generated by Django 4.1 on 2022-11-27 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalExpenses', '0015_remove_userexpense_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userexpense',
            old_name='expense',
            new_name='monthly_earning',
        ),
        migrations.RenameField(
            model_name='userexpense',
            old_name='income',
            new_name='monthly_expenses',
        ),
        migrations.RenameField(
            model_name='userexpense',
            old_name='saving',
            new_name='monthly_savings',
        ),
    ]
