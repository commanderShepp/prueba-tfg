# Generated by Django 3.0.4 on 2020-05-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0006_auto_20200506_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuento',
            name='texto',
        ),
        migrations.AddField(
            model_name='cuento',
            name='fpage',
            field=models.CharField(default='nada', max_length=10000, verbose_name='ppagina'),
        ),
        migrations.AddField(
            model_name='cuento',
            name='spage',
            field=models.CharField(default='nada', max_length=10000, verbose_name='spagina'),
        ),
        migrations.AddField(
            model_name='cuento',
            name='tpage',
            field=models.CharField(default='nada', max_length=10000, verbose_name='tpagina'),
        ),
    ]
