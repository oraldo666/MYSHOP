# Generated by Django 4.0.5 on 2022-06-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]