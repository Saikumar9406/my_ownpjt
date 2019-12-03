# Generated by Django 2.2.7 on 2019-11-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addcontestent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestent_name', models.CharField(max_length=20)),
                ('proffession', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('image', models.ImageField(upload_to='profile_image')),
            ],
        ),
    ]
