# Generated by Django 2.2.7 on 2019-11-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbossapp', '0004_regmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcontestent',
            old_name='dob',
            new_name='born',
        ),
        migrations.RenameField(
            model_name='addcontestent',
            old_name='proffession',
            new_name='ocuupation',
        ),
        migrations.AddField(
            model_name='addcontestent',
            name='gender',
            field=models.CharField(default=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addcontestent',
            name='origin',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]
