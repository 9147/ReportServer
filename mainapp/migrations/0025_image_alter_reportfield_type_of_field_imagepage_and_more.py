# Generated by Django 5.0.3 on 2024-04-29 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_alter_reportfield_type_of_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('text', 'Text'), ('time', 'Time'), ('datetime', 'Date and Time'), ('date', 'Date'), ('image', 'Image'), ('integer', 'Integer')], default='text', max_length=100),
        ),
        migrations.CreateModel(
            name='ImagePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mainapp/static/backgrounds/')),
                ('images', models.ManyToManyField(blank=True, related_name='image_page_images', to='mainapp.image')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='Image_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_image_page', to='mainapp.imagepage'),
        ),
    ]
