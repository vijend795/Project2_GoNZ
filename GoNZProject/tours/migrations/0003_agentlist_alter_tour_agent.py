# Generated by Django 4.2.4 on 2023-08-18 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tours', '0002_tour_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agents', models.ManyToManyField(related_name='agent_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='tour',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.agentlist', verbose_name='Agent Name'),
        ),
    ]
