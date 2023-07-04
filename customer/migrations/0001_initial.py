# Generated by Django 4.1.7 on 2023-06-19 15:41

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
                ('mobile_number', models.CharField(max_length=20, unique=True)),
                ('telegram_uid', models.CharField(blank=True, max_length=20, null=True)),
                ('has_visit_telegram', models.BooleanField(default=False)),
            ],
        ),
    ]