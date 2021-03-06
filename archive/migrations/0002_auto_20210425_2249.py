# Generated by Django 3.1.6 on 2021-04-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=9)),
                ('access_level', models.CharField(max_length=1)),
                ('content', models.CharField(max_length=100000)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='access_level',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
