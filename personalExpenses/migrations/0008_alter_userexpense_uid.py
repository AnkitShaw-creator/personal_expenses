# Generated by Django 4.1 on 2022-11-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalExpenses', '0007_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexpense',
            name='uid',
            field=models.TextField(max_length=10, null=True),
        ),
    ]
