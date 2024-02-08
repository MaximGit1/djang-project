# Generated by Django 5.0.1 on 2024-02-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0009_alter_book_book_image_alter_book_epub_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%mh0u6f2x5m2v0'),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(upload_to='books/%Y/%mh0u6f2x5m2v0'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%mh0u6f2x5m2v0'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(upload_to='books/%Y/%mh0u6f2x5m2v0'),
        ),
    ]