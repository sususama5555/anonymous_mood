# Generated by Django 2.2.6 on 2020-07-15 13:01

from django.db import migrations, models
import mood.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='创建人')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否软删除')),
                ('content', models.TextField(max_length=1000, verbose_name='内容')),
                ('image', models.ImageField(blank=True, max_length=1000, null=True, upload_to=mood.models.user_directory_path, verbose_name='附图')),
                ('click_counter', models.IntegerField(default=0, verbose_name='点击数')),
                ('collect_counter', models.IntegerField(default=0, verbose_name='收藏数')),
                ('like_counter', models.IntegerField(default=0, verbose_name='点赞数')),
            ],
            options={
                'verbose_name': '心情',
                'verbose_name_plural': '心情',
                'ordering': ('create_at',),
            },
        ),
    ]