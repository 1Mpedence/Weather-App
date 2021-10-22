# Generated by Django 3.2.8 on 2021-10-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon_id', models.CharField(max_length=5)),
                ('temperature', models.IntegerField()),
                ('description', models.TextField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
