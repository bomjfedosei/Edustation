# Generated by Django 2.2.3 on 2019-07-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_connections'),
    ]

    operations = [
        migrations.AddField(
            model_name='botdialog',
            name='owner',
            field=models.BooleanField(default='False', verbose_name='Принадлежность боту(если checkbox стоит, то боту принадлежит)'),
            preserve_default=False,
        ),
    ]
