# Generated by Django 4.2.1 on 2024-06-18 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
