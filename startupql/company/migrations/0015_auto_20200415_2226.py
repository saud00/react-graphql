# Generated by Django 3.0.4 on 2020-04-15 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_auto_20200415_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='Link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='company.link'),
        ),
    ]