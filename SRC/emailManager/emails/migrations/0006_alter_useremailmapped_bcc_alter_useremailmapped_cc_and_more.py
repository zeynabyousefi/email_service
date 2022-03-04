# Generated by Django 4.0.2 on 2022-02-28 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emails', '0005_remove_email_bcc_remove_email_cc_useremailmapped_bcc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailmapped',
            name='bcc',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='useremailmapped',
            name='cc',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='useremailmapped',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
