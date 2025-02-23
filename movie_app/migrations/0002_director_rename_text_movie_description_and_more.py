# Generated by Django 5.1.4 on 2025-02-07 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='price',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='created',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='updated',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_app.director'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie')),
            ],
        ),
    ]
