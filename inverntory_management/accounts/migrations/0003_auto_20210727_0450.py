# Generated by Django 3.2.5 on 2021-07-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_my_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='my_user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='my_user',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='my_user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='my_user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
