# Generated by Django 3.0.2 on 2020-03-24 06:29

from django.db import migrations, models
import tweet.utils


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20200322_0845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=100, validators=[tweet.utils.validateText]),
        ),
    ]
