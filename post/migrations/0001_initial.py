# Generated by Django 2.2 on 2020-04-07 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=32, unique=True, verbose_name='类别名称')),
            ],
            options={
                'db_table': 't_category',
                'verbose_name_plural': '类别',
                'verbose_name': '类别',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=32, unique=True, verbose_name='标签名称')),
            ],
            options={
                'db_table': 't_tag',
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='标题')),
                ('desc', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Category')),
                ('tag', models.ManyToManyField(to='post.Tag')),
            ],
            options={
                'db_table': 't_post',
                'verbose_name_plural': '帖子',
                'verbose_name': '帖子',
            },
        ),
    ]