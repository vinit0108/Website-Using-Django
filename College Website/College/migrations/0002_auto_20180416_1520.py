# Generated by Django 2.0.4 on 2018-04-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('ratings', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employe',
        ),
    ]
