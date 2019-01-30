# Generated by Django 2.1 on 2019-01-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=100)),
                ('description_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_choice', models.CharField(max_length=100)),
                ('vote_date', models.DateTimeField(verbose_name='Date Voted')),
            ],
        ),
    ]
