# Generated by Django 5.1.2 on 2024-10-25 10:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listor', '0002_alter_item_amount_alter_item_item_name_sharedlisr'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SharedLisr',
            new_name='SharedList',
        ),
    ]
