# Generated by Django 4.1.6 on 2023-02-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=20)),
                ('telegram_uid', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
