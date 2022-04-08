# Generated by Django 4.0.3 on 2022-04-08 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=8000)),
                ('type', models.CharField(choices=[('back-end', 'BACK-END'), ('front-end', 'FRONT-END'), ('iOS', 'iOS'), ('android', 'ANDROID')], max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=8000)),
                ('tag', models.CharField(choices=[('bug', 'BUG'), ('amélioration', 'AMELIORATION'), ('tâche', 'TACHE')], max_length=100)),
                ('priority', models.CharField(choices=[('faible', 'FAIBLE'), ('moyen', 'MOYENNE'), ('elevee', 'ÉLEVÉE')], max_length=100)),
                ('status', models.CharField(choices=[('à faire', 'A FAIRE'), ('en cours', 'EN COURS'), ('terminé', 'TERMINE')], max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues_project', to='application.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('AUTHOR', 'Auther'), ('CONTRIBUTOR', 'Contributor')], max_length=50)),
                ('role', models.CharField(choices=[('AUTHOR', 'Auther'), ('CONTRIBUTOR', 'Contributor')], max_length=100)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor_user', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributor_project', to='application.project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=8000)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='application.issue')),
            ],
        ),
    ]
