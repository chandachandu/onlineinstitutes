# Generated by Django 3.0.5 on 2020-07-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_scheduleclassestable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleclassestable',
            name='name',
        ),
    ]
