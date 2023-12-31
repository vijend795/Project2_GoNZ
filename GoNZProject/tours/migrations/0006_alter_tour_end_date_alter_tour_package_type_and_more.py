# Generated by Django 4.2.4 on 2023-08-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_tour_agent_delete_agentlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='end_date',
            field=models.DateField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='tour',
            name='package_type',
            field=models.CharField(blank=True, choices=[('Basic', 'Basic'), ('Platinum', 'Platinum'), ('Gold', 'Gold')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_date',
            field=models.DateField(blank=True, verbose_name=''),
        ),
    ]
