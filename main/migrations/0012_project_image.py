# Generated by Django 5.0.1 on 2024-01-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_skill_topskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/projects'),
        ),
    ]
