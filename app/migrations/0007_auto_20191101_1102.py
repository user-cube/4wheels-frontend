# Generated by Django 2.2.6 on 2019-11-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_carrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='id',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='auto_increment_id',
            field=models.AutoField(default=9999, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]