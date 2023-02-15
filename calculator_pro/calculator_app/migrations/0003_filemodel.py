# Generated by Django 4.1.1 on 2022-10-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0002_reg2model'),
    ]

    operations = [
        migrations.CreateModel(
            name='filemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=20)),
                ('iprice', models.IntegerField()),
                ('des', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='calculator_app/static')),
            ],
        ),
    ]