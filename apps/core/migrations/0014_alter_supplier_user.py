# Generated by Django 3.2.16 on 2022-10-21 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_supplier_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
