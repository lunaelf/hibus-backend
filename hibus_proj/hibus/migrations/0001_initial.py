# Generated by Django 3.1.4 on 2020-12-10 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=20, unique=True)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('threshold_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('current_passenger', models.PositiveIntegerField(default=0)),
                ('threshold_passenger', models.PositiveIntegerField()),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('location', models.CharField(default='', max_length=200)),
                ('station', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_start', models.CharField(max_length=50)),
                ('station_end', models.CharField(max_length=50)),
                ('estimate_hour', models.PositiveIntegerField()),
                ('estimate_minute', models.PositiveIntegerField()),
                ('start_latitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('start_longitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('start_location', models.CharField(default='', max_length=200)),
                ('end_latitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('end_longitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('end_location', models.CharField(default='', max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.UUIDField(editable=False)),
                ('base_order_number', models.UUIDField(editable=False)),
                ('order_type', models.IntegerField()),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('passenger', models.PositiveIntegerField(default=1)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.IntegerField(default=0)),
                ('bus_start_time', models.DateTimeField()),
                ('bus_end_time', models.DateTimeField()),
                ('station_start', models.CharField(max_length=50)),
                ('station_end', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hibus.bus')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hibus.line')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='bus',
            name='line_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hibus.line'),
        ),
    ]
