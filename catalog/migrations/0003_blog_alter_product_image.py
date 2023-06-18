# Generated by Django 4.2.1 on 2023-06-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_product_category_product_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='содержимое')),
                ('image', models.ImageField(upload_to='Blog/', verbose_name='превью')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_public', models.BooleanField(default=True, verbose_name='публикация')),
                ('num_views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Product/', verbose_name='превью'),
        ),
    ]