# Generated by Django 3.2.7 on 2021-10-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('gross', models.IntegerField(help_text='По всему миру, в гривнах.', verbose_name='Сборы')),
            ],
        ),
    ]
