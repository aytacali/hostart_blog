# Generated by Django 4.1.1 on 2022-09-28 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_blog_user_alter_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.AddField(
            model_name='blog',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='LikeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.blog')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
