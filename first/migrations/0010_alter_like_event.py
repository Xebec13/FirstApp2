# Generated by Django 4.2.6 on 2023-11-01 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0009_event_total_dislikes_event_total_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_likes', to='first.event'),
        ),
    ]
