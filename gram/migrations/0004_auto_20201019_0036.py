# Generated by Django 3.1 on 2020-10-19 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_auto_20201019_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gram.profile'),
        ),
    ]
