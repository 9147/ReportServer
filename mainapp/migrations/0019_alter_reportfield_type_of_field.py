# Generated by Django 5.0 on 2024-03-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_class_development_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('time', 'Time'), ('integer', 'Integer'), ('text', 'Text'), ('datetime', 'Date and Time'), ('date', 'Date'), ('image', 'Image')], default='text', max_length=100),
        ),
    ]
