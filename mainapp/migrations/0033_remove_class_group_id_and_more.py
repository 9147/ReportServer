# Generated by Django 5.0.3 on 2024-06-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0032_alter_class_group_id_alter_reportfield_type_of_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='group_id',
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('time', 'Time'), ('date', 'Date'), ('image', 'Image'), ('datetime', 'Date and Time')], default='text', max_length=100),
        ),
    ]
