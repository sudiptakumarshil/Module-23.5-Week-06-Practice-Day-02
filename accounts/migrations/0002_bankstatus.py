# Generated by Django 5.0.6 on 2024-08-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_bankrupt', models.BooleanField(db_comment='Yes/No')),
            ],
        ),
    ]
