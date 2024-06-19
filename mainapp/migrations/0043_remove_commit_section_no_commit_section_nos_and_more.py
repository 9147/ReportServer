# Generated by Django 5.0.3 on 2024-06-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_commit_section_no_alter_reportfield_type_of_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commit',
            name='section_no',
        ),
        migrations.AddField(
            model_name='commit',
            name='section_nos',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('integer', 'Integer'), ('text', 'Text'), ('datetime', 'Date and Time'), ('time', 'Time'), ('image', 'Image'), ('date', 'Date')], default='text', max_length=100),
        ),
    ]
