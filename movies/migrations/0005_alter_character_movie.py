# Generated by Django 3.2.5 on 2021-10-22 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_character_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]
