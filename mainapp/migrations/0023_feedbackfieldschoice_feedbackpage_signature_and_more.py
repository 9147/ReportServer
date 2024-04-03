# Generated by Django 5.0.3 on 2024-04-03 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_class_default_background_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackFieldsChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('required', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='reportfield',
            name='type_of_field',
            field=models.CharField(choices=[('date', 'Date'), ('integer', 'Integer'), ('datetime', 'Date and Time'), ('image', 'Image'), ('text', 'Text'), ('time', 'Time')], default='text', max_length=100),
        ),
        migrations.CreateModel(
            name='FeedbackField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('options', models.ManyToManyField(blank=True, related_name='feedback_field_options', to='mainapp.feedbackfieldschoice')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='feedback_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_feedback_page', to='mainapp.feedbackpage'),
        ),
        migrations.CreateModel(
            name='FeedbackSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Fields', models.ManyToManyField(blank=True, related_name='feedback_section_fields', to='mainapp.feedbackfield')),
            ],
        ),
        migrations.AddField(
            model_name='feedbackpage',
            name='sections',
            field=models.ManyToManyField(blank=True, related_name='feedback_page_section', to='mainapp.feedbacksection'),
        ),
        migrations.AddField(
            model_name='feedbackpage',
            name='signature',
            field=models.ManyToManyField(blank=True, related_name='feedback_page_signature', to='mainapp.signature'),
        ),
    ]