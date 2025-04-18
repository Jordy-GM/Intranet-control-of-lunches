# Generated by Django 5.1 on 2024-10-03 17:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks1', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(max_length=100)),
                ('option_number', models.IntegerField()),
                ('soup', models.CharField(max_length=100)),
                ('rice', models.CharField(max_length=100)),
                ('protein', models.CharField(max_length=100)),
                ('guarnicion', models.CharField(max_length=100)),
                ('salad', models.CharField(max_length=100)),
                ('drink', models.CharField(max_length=100)),
                ('dessert', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Menuselection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_selected', models.DateTimeField(auto_now_add=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_selections', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_selections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
