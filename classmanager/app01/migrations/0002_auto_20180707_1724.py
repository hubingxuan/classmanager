# Generated by Django 2.0.1 on 2018-07-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cs',
            field=models.ForeignKey(on_delete=True, related_name='test', to='app01.Class'),
        ),
    ]
