# Generated by Django 3.0.6 on 2020-05-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20200526_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(default='app/static/img/default_item.jpg', upload_to='app/static/img/item/1144056290/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/1144056290/'),
        ),
    ]
