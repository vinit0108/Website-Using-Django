# Generated by Django 2.0.4 on 2018-04-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title1', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('title3', models.CharField(max_length=100)),
                ('title4', models.CharField(max_length=100)),
                ('title5', models.CharField(max_length=100)),
            ],
        ),
    ]
