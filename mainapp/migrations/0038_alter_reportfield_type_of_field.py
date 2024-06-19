# Generated by Django 5.0.3 on 2024-06-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_alter_reportfield_type_of_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('datetime', 'Date and Time'), ('date', 'Date'), ('image', 'Image'), ('time', 'Time'), ('integer', 'Integer'), ('text', 'Text')], default='text', max_length=100),
        ),
    ]
