# Generated by Django 4.1.2 on 2022-11-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_commentimage_parent_remove_comments_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='<Zar>', max_length=256),
        ),
    ]
