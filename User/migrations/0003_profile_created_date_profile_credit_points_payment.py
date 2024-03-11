# Generated by Django 5.0.2 on 2024-03-11 14:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_profile_dob_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='credit_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('transcation_id', models.CharField(blank=True, max_length=52, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('payment_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.profile')),
            ],
        ),
    ]