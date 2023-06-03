# Generated by Django 4.1.3 on 2022-12-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fa', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]