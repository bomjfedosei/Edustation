# Generated by Django 2.2.3 on 2019-07-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_auto_20190706_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='page_title',
            field=models.CharField(default='anime', max_length=5, verbose_name='Ссылка на страницу'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courses',
            name='type',
            field=models.CharField(max_length=50, verbose_name='Тип курса'),
        ),
    ]
