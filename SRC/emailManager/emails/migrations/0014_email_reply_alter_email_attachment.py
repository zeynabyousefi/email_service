# Generated by Django 4.0.2 on 2022-03-03 16:09

from django.db import migrations, models
import django.db.models.deletion
import emails.validators


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0013_alter_email_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='emails.email'),
        ),
        migrations.AlterField(
            model_name='email',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='<function user_directory_path at 0x000001668D523910>/', validators=[emails.validators.validate_file_size]),
        ),
    ]
