# Generated by Django 4.2.6 on 2023-10-31 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_user_event_owner_alter_reservation_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
    ]
