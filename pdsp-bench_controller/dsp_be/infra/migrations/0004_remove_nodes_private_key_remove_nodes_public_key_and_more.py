# Generated by Django 4.1.4 on 2023-02-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0003_nodes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodes',
            name='private_key',
        ),
        migrations.RemoveField(
            model_name='nodes',
            name='public_key',
        ),
        migrations.AddField(
            model_name='cluster',
            name='slave_node_ip',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]