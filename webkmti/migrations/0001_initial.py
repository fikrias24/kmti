# Generated by Django 5.1.1 on 2025-03-08 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id_candidate', models.AutoField(primary_key=True, serialize=False)),
                ('nama_candidate', models.CharField(max_length=100)),
                ('visi', models.TextField()),
                ('misi', models.TextField()),
                ('jumlah_vote', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='voter',
            fields=[
                ('id_voter', models.AutoField(primary_key=True, serialize=False)),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('nim', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id_vote', models.AutoField(primary_key=True, serialize=False)),
                ('waktu_vote', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkmti.candidate')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkmti.voter')),
            ],
        ),
    ]
