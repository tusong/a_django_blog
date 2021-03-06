# Generated by Django 2.0.1 on 2018-01-09 10:25

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('head_pic_url', models.CharField(default='/static/img/default.jpg', max_length=250, verbose_name='头图链接')),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('brief', models.CharField(blank=True, max_length=200, null=True, verbose_name='摘要')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='正文')),
                ('page_views', models.PositiveIntegerField(default=0, editable=False, verbose_name='阅读量')),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_1', models.CharField(db_index=True, max_length=30, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_2', models.CharField(db_index=True, max_length=30, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('friend_url', models.CharField(default='http://', max_length=250, verbose_name='链接')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Friend_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=30, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('head_pic_url', models.CharField(blank=True, default='/static/img/default.jpg', max_length=250, null=True, verbose_name='头图链接')),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='正文')),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Profile_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=30, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=30, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Profile_Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='friend',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Friend_Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category1', verbose_name='一级目录'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category2', verbose_name='二级目录'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签'),
        ),
    ]
