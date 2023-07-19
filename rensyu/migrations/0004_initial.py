# Generated by Django 4.2.3 on 2023-07-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rensyu', '0003_delete_tranditionalcolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranditionalColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(help_text='색깔 이름', max_length=50)),
                ('category_code', models.CharField(help_text='카테고리 코드', max_length=4)),
                ('rgb_code', models.CharField(help_text='rgb 코드', max_length=6)),
                ('r_num', models.IntegerField(help_text='r값')),
                ('g_num', models.IntegerField(help_text='g값')),
                ('b_num', models.IntegerField(help_text='b값')),
                ('cymk_code', models.CharField(help_text='cymk 코드', max_length=6)),
            ],
        ),
    ]
