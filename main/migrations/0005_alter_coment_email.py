# Generated by Django 4.2.8 on 2024-07-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
