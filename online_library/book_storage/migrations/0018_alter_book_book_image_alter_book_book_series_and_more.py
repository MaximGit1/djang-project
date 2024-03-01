# Generated by Django 5.0.1 on 2024-03-01 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0017_bookseries_alter_book_book_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%mm8f1f5h0j4l6'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book_storage.bookseries'),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mm8f1f5h0j4l6'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%mm8f1f5h0j4l6'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mm8f1f5h0j4l6'),
        ),
    ]
