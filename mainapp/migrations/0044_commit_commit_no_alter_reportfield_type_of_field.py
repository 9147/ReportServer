# Generated by Django 5.0.3 on 2024-06-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0043_remove_commit_section_no_commit_section_nos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='commit_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('date', 'Date'), ('text', 'Text'), ('integer', 'Integer'), ('time', 'Time'), ('datetime', 'Date and Time'), ('image', 'Image')], default='text', max_length=100),
        ),
    ]
