# Generated by Django 3.1.7 on 2024-02-28 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compete', '0002_alter_compete_compete_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applycompete',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='compete',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='province',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
