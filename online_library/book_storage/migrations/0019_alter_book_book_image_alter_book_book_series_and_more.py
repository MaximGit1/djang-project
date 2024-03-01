# Generated by Django 5.0.1 on 2024-03-01 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0018_alter_book_book_image_alter_book_book_series_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%mj0g6b4n8v6u7'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='book_storage.bookseries'),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mj0g6b4n8v6u7'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%mj0g6b4n8v6u7'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mj0g6b4n8v6u7'),
        ),
    ]
