# Generated by Django 5.1.4 on 2024-12-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_baseuser_options_alter_commonuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonuser',
            name='national_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
