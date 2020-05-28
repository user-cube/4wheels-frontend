# Generated by Django 2.2.6 on 2019-11-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20191102_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.CharField(default='ruioc', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/-1875636296/'),
        ),
    ]
