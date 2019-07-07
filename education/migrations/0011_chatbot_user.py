# Generated by Django 2.2.3 on 2019-07-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0010_auto_20190706_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbot_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('serialkeys', models.UUIDField(verbose_name='UUID')),
            ],
        ),
    ]