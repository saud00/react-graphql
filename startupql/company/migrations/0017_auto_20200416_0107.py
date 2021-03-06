# Generated by Django 3.0.4 on 2020-04-15 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0016_auto_20200415_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employ',
            name='Link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='company.link'),
        ),
    ]
