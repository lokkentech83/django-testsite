# Generated by Django 4.2.3 on 2023-07-14 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rensyu', '0006_tranditionalcolorcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='b_num',
            new_name='b값',
        ),
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='cymk_code',
            new_name='cymk 코드',
        ),
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='g_num',
            new_name='g값',
        ),
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='rgb_code',
            new_name='rgb 코드',
        ),
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='r_num',
            new_name='r값',
        ),
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='color_name',
            new_name='색깔 이름',
        ),
        migrations.RenameField(
            model_name='tranditionalcolor',
            old_name='category_code',
            new_name='카테고리 코드',
        ),
    ]
