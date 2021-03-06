# Generated by Django 2.0.6 on 2018-06-21 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('iid', models.IntegerField(primary_key=True, serialize=False)),
                ('ttype', models.CharField(max_length=50)),
                ('icode', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Wfdata',
            fields=[
                ('iid', models.IntegerField(primary_key=True, serialize=False)),
                ('barcode', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('t_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Transaction')),
            ],
        ),
    ]
