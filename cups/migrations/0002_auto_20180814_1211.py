# Generated by Django 2.0.5 on 2018-08-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
