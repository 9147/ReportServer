# Generated by Django 5.0.3 on 2024-06-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_rename_addmission_no_commit_admission_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='section_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('date', 'Date'), ('image', 'Image'), ('integer', 'Integer'), ('datetime', 'Date and Time'), ('text', 'Text'), ('time', 'Time')], default='text', max_length=100),
        ),
    ]
