# Generated by Django 2.1.1 on 2018-10-15 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oj_base', '0002_remove_new_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
