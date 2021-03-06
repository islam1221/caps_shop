# Generated by Django 4.0 on 2021-12-23 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cap',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cap',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cap',
            name='imege',
            field=models.ImageField(upload_to=''),
        ),
        migrations.RemoveField(
            model_name='cap',
            name='size',
        ),
        migrations.AddField(
            model_name='cap',
            name='size',
            field=models.ManyToManyField(to='main.Size'),
        ),
    ]
