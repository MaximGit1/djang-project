# Generated by Django 5.0.1 on 2024-03-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0004_alter_book_book_image_alter_book_epub_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%mo5i3m0y5b2a9', verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mo5i3m0y5b2a9', verbose_name='epub файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%mo5i3m0y5b2a9', verbose_name='fb2 файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mo5i3m0y5b2a9', verbose_name='mp3 файл'),
        ),
    ]
