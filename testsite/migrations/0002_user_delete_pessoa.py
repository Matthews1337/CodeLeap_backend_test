# Generated by Django 4.2.6 on 2024-04-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
