# Generated by Django 3.0 on 2020-05-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_freelancerskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreelancerPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=20)),
                ('payment_date', models.DateField()),
            ],
        ),
    ]
