# Generated by Django 3.2.4 on 2021-06-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studycafe', '0002_auto_20210629_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='studycafe',
            name='img',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
