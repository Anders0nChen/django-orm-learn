# Generated by Django 2.0.6 on 2018-06-14 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedCharField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher_list'),
        ),
        migrations.AlterModelTable(
            name='person',
            table='person_table',
        ),
    ]