# Generated by Django 3.0 on 2020-05-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreelancerSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
            ],
        ),
    ]
