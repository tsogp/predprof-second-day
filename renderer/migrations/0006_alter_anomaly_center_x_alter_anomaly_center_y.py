# Generated by Django 4.0 on 2022-04-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renderer', '0005_alter_anomaly_center_x_alter_anomaly_center_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anomaly',
            name='center_x',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='anomaly',
            name='center_y',
            field=models.FloatField(null=True),
        ),
    ]