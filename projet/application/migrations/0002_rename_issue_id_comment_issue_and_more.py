# Generated by Django 4.0.3 on 2022-03-07 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='issue_id',
            new_name='issue',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
    ]