# Generated by Django 4.2.3 on 2023-07-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rensyu', '0014_delete_codelist_delete_codemanage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
            ],
        ),
    ]
