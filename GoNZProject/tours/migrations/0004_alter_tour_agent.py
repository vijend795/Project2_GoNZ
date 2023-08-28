# Generated by Django 4.2.4 on 2023-08-18 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_agentlist_alter_tour_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.agentlist', verbose_name='Agent Name'),
        ),
    ]
