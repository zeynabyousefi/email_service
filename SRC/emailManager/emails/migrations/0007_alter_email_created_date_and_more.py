# Generated by Django 4.0.2 on 2022-02-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0006_alter_useremailmapped_bcc_alter_useremailmapped_cc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='created_date',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='useremailmapped',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useremailmapped',
            name='is_starred',
            field=models.BooleanField(default=False),
        ),
    ]
