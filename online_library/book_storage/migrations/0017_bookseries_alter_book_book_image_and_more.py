# Generated by Django 5.0.1 on 2024-03-01 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0016_alter_book_book_image_alter_book_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_series', models.CharField(max_length=35)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%ms0y6l7p5b4j8'),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%ms0y6l7p5b4j8'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%ms0y6l7p5b4j8'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%ms0y6l7p5b4j8'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_series',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='book_storage.bookseries'),
        ),
    ]
