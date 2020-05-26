# Generated by Django 3.0 on 2020-05-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_skillcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=50)),
                ('date_earned', models.DateField()),
                ('updated_date', models.DateField()),
            ],
        ),
    ]
