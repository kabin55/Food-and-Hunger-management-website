# Generated by Django 5.0.1 on 2024-03-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='phone',
        ),
    ]
