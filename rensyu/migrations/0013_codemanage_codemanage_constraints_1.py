# Generated by Django 4.2.3 on 2023-07-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rensyu', '0012_remove_codemanage_codemanage_constraints_1'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='codemanage',
            constraint=models.UniqueConstraint(fields=('code', 'code_subcode'), name='CodeManage_constraints_1'),
        ),
    ]