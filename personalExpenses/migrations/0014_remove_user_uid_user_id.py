# Generated by Django 4.1 on 2022-11-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalExpenses', '0013_alter_userexpense_expense_alter_userexpense_income_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
