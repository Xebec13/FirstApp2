# Generated by Django 4.2.6 on 2023-10-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_guest_delete_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='events', to='first.user'),
        ),
    ]
