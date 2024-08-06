# Generated by Django 4.2.1 on 2024-07-23 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_alter_todo_forget_password_token_alter_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
