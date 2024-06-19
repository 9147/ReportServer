# Generated by Django 5.0.3 on 2024-06-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_commit_alter_reportfield_type_of_field_classcommit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commit',
            old_name='addmission_no',
            new_name='admission_no',
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('date', 'Date'), ('integer', 'Integer'), ('time', 'Time'), ('datetime', 'Date and Time'), ('text', 'Text'), ('image', 'Image')], default='text', max_length=100),
        ),
    ]