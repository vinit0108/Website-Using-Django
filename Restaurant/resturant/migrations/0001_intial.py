# Generated by Django 2.0.3 on 2018-03-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('dishes', models.CharField(max_length=300)),
                ('rating', models.IntegerField(max_length=10))
            ],
        ),
    ]