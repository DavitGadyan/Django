# Generated by Django 3.2.3 on 2021-05-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('capital', models.CharField(default='', max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
