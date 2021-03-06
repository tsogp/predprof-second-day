# Generated by Django 4.0 on 2022-04-17 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_x', models.FloatField()),
                ('center_y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coord', models.FloatField()),
                ('y_coord', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DetectAnomaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('anomaly_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renderer.anomaly')),
                ('detector_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renderer.detector')),
            ],
        ),
    ]
