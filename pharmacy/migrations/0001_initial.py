# Generated by Django 4.1.6 on 2023-02-03 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drug', '0002_alter_drug_description'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_export', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('drugs', models.ManyToManyField(to='drug.drug')),
            ],
        ),
    ]
