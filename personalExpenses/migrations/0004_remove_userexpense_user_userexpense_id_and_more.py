# Generated by Django 4.1 on 2022-11-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalExpenses', '0003_remove_userexpense_id_userexpense_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userexpense',
            name='user',
        ),
        migrations.AddField(
            model_name='userexpense',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userexpense',
            name='uid',
            field=models.TextField(),
        ),
    ]
