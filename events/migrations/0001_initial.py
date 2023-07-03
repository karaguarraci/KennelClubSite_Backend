# Generated by Django 4.2.2 on 2023-07-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]