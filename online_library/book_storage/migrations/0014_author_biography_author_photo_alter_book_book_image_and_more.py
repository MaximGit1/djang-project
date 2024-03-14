# Generated by Django 5.0.1 on 2024-02-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0013_alter_book_book_image_alter_book_epub_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, max_length=2100),
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, upload_to='authors/avatar'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%mk4j5k4s3g6a2'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=750),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mk4j5k4s3g6a2'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%mk4j5k4s3g6a2'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mk4j5k4s3g6a2'),
        ),
    ]
