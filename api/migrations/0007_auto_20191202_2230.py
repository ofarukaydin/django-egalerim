# Generated by Django 2.2.3 on 2019-12-02 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191202_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cariler',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to=settings.AUTH_USER_MODEL),
        ),
    ]