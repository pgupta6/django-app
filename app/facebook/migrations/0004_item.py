# Generated by Django 3.2.25 on 2024-09-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_comment_postid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=255)),
            ],
        ),
    ]
