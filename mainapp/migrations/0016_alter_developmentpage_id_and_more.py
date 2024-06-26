# Generated by Django 5.0 on 2024-03-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_developmentpage_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developmentpage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('datetime', 'Date and Time'), ('date', 'Date'), ('image', 'Image'), ('integer', 'Integer'), ('text', 'Text'), ('time', 'Time')], default='text', max_length=100),
        ),
    ]
