# Generated by Django 5.0.9 on 2024-11-17 21:36

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_purchased', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Flat',
                'verbose_name_plural': 'Flats',
            },
        ),
        migrations.CreateModel(
            name='IPFSLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cid', models.CharField(max_length=255, unique=True)),
                ('link', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name': 'IPFS Link',
                'verbose_name_plural': 'IPFS Links',
            },
        ),
        migrations.CreateModel(
            name='FlatImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='flat.flat')),
            ],
            options={
                'verbose_name': 'Flat Image',
                'verbose_name_plural': 'Flat Images',
            },
        ),
    ]
