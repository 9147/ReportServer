# Generated by Django 5.0.3 on 2024-06-02 13:04

import mainapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_populate_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='group_id',
            field=models.CharField(blank=True, default=mainapp.models.generate_unique_code, editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('time', 'Time'), ('datetime', 'Date and Time'), ('text', 'Text'), ('integer', 'Integer'), ('image', 'Image'), ('date', 'Date')], default='text', max_length=100),
        ),
    ]
