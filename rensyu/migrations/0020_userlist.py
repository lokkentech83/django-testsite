# Generated by Django 4.2.3 on 2023-07-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rensyu', '0019_codemanage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanzi_name', models.CharField(max_length=50)),
                ('kana_name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=4)),
                ('blood_type', models.CharField(max_length=4)),
                ('mail_address', models.CharField(max_length=100)),
                ('tel_num', models.CharField(max_length=15)),
                ('mobile_tel_num', models.CharField(max_length=15)),
                ('post_num', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=50)),
            ],
        ),
    ]
