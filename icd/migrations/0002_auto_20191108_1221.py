# Generated by Django 2.0.3 on 2019-11-08 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='HBABitmap',
        ),
        migrations.RemoveField(
            model_name='station',
            name='LBABitmap',
        ),
        migrations.RemoveField(
            model_name='station',
            name='ReceiverBitmap',
        ),
    ]
