# Generated by Django 4.1 on 2022-11-25 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalExpenses', '0008_alter_userexpense_uid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='userExpense',
        ),
    ]
