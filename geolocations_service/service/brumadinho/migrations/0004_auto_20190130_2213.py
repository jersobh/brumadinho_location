# Generated by Django 2.1.3 on 2019-01-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brumadinho', '0003_geolocation_radius'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geolocation',
            name='radius',
        ),
        migrations.AddField(
            model_name='visitedlocation',
            name='observations',
            field=models.CharField(blank=True, help_text='Observations', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='visitedlocation',
            name='radius',
            field=models.FloatField(default=1, help_text='Radial área range of search.'),
        ),
    ]
