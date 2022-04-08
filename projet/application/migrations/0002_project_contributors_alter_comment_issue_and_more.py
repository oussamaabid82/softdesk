# Generated by Django 4.0.3 on 2022-04-08 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(related_name='contributions', through='application.Contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_issue', to='application.issue'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='assignee_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together={('author_user', 'project')},
        ),
    ]
