# Generated by Django 5.0.3 on 2024-03-10 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_rename_aadress_company_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
