# Generated by Django 4.0.5 on 2023-05-23 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_carusel_body_en_carusel_body_uz_carusel_title_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
    ]
