# Generated by Django 5.0.4 on 2024-05-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='course',
            field=models.CharField(default='100', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.CharField(default='100', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default='100', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]