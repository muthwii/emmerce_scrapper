# Generated by Django 4.0.6 on 2022-07-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotpointCategories2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'HotpointCategories',
                'verbose_name_plural': 'HotpointCategories',
            },
        ),
        migrations.CreateModel(
            name='HotpointProductLinks2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'HotpointProductLinks',
                'verbose_name_plural': 'HotpointProductLinks',
            },
        ),
        migrations.CreateModel(
            name='HypermartCategories2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, max_length=900, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'HypermartCategories',
                'verbose_name_plural': 'HypermartCategories',
            },
        ),
        migrations.CreateModel(
            name='HypermartProductLinks2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'HypermartProductLinks',
                'verbose_name_plural': 'HypermartProductLinks',
            },
        ),
        migrations.CreateModel(
            name='MikaCategories2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'MikaCategories',
                'verbose_name_plural': 'MikaCategories',
            },
        ),
        migrations.CreateModel(
            name='MikaProductLinks2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'MikaProductLinks',
                'verbose_name_plural': 'MikaProductLinks',
            },
        ),
        migrations.CreateModel(
            name='OpalnetCategories2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'OpalnetCategories',
                'verbose_name_plural': 'OpalnetCategories',
            },
        ),
        migrations.CreateModel(
            name='OpalnetProductLinks2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'OpalnetProductLinks',
                'verbose_name_plural': 'OpalnetProductLinks',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(blank=True, max_length=10000, null=True)),
                ('regular_price', models.TextField(blank=True, max_length=10000, null=True)),
                ('sale_price', models.TextField(blank=True, max_length=10000, null=True)),
                ('brand', models.TextField(blank=True, max_length=10000, null=True)),
                ('upc', models.TextField(blank=True, max_length=10000, null=True)),
                ('sku', models.TextField(blank=True, max_length=10000, null=True)),
                ('product_link', models.TextField(blank=True, null=True)),
                ('stock_status', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
