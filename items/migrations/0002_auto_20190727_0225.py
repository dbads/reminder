# Generated by Django 2.2.3 on 2019-07-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('items_available', models.CharField(blank=True, max_length=1000, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'shop_table',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
