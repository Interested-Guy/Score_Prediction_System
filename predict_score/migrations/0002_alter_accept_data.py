# Generated by Django 3.2.12 on 2001-12-31 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_score', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept',
            name='data',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
