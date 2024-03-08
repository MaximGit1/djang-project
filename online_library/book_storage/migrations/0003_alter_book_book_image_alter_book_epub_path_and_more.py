# Generated by Django 5.0.1 on 2024-03-07 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0002_alter_book_book_image_alter_book_epub_path_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='books/%Y/%mq8p5g3d2k5z7', verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mq8p5g3d2k5z7', verbose_name='epub файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='fb2_path',
            field=models.FileField(upload_to='books/%Y/%mq8p5g3d2k5z7', verbose_name='fb2 файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mp3_path',
            field=models.FileField(blank=True, upload_to='books/%Y/%mq8p5g3d2k5z7', verbose_name='mp3 файл'),
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_storage.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]