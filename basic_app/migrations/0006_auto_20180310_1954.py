# Generated by Django 2.0.2 on 2018-03-10 16:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20170307_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete='on_delete', to=settings.AUTH_USER_MODEL),
        ),
    ]
