# Generated by Django 3.0.4 on 2020-04-14 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20200414_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='Link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='company.link'),
        ),
    ]
