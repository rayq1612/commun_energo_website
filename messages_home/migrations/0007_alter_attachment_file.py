# Generated by Django 4.2 on 2023-05-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('messages_home', '0006_alter_attachment_file_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='attachments/'),
        ),
    ]
