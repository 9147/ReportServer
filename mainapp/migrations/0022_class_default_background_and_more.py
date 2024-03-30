# Generated by Django 5.0 on 2024-03-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_alter_reportfield_type_of_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='default_background',
            field=models.ImageField(blank=True, null=True, upload_to='mainapp/static/backgrounds/'),
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('time', 'Time'), ('text', 'Text'), ('date', 'Date'), ('datetime', 'Date and Time'), ('image', 'Image'), ('integer', 'Integer')], default='text', max_length=100),
        ),
    ]
