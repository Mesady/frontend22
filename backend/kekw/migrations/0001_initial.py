# Generated by Django 4.1.3 on 2022-12-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.URLField(max_length=500)),
                ('radiourl', models.URLField(max_length=500)),
            ],
        ),
    ]