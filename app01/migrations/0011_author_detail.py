# Generated by Django 2.0.6 on 2018-06-14 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20180614_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app01.AuthorDetail'),
        ),
    ]
