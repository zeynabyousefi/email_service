# Generated by Django 4.0.2 on 2022-03-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0026_alter_filter_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='file_size',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
