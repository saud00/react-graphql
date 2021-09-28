# Generated by Django 3.0.4 on 2020-04-11 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.TextField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=22)),
                ('E_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='E_city', to='company.city')),
            ],
        ),
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=22)),
            ],
        ),
        migrations.DeleteModel(
            name='emp',
        ),
        migrations.AddField(
            model_name='employ',
            name='E_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='E_title', to='company.title'),
        ),
        migrations.AddField(
            model_name='employ',
            name='Link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='company.link'),
        ),
    ]