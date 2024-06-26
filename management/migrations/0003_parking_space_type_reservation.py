# Generated by Django 4.2.3 on 2024-04-24 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_parking_num_spaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='space_type',
            field=models.CharField(choices=[('CONVENTIONAL', 'Convencional'), ('PRIORITY', 'Prioritária')], default='Convencional', max_length=20),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('parking_space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.parkingspace')),
            ],
        ),
    ]
