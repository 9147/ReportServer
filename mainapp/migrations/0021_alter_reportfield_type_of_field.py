# Generated by Django 5.0 on 2024-03-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_rename_section_developmentpage_sections_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('time', 'Time'), ('image', 'Image'), ('date', 'Date'), ('integer', 'Integer'), ('text', 'Text'), ('datetime', 'Date and Time')], default='text', max_length=100),
        ),
    ]
