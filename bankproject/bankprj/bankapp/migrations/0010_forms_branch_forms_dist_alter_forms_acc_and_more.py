# Generated by Django 4.2.3 on 2023-07-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0009_remove_forms_branch_remove_forms_dist'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='branch',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='forms',
            name='dist',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='forms',
            name='acc',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='forms',
            name='gender',
            field=models.CharField(default=True, max_length=10),
        ),
    ]