# Generated by Django 4.1 on 2022-11-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalExpenses', '0016_rename_expense_userexpense_monthly_earning_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexpense',
            name='monthly_earning',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userexpense',
            name='monthly_expenses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userexpense',
            name='monthly_savings',
            field=models.IntegerField(default=0),
        ),
    ]
