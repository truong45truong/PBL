# Generated by Django 4.0.5 on 2022-10-21 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.categories')),
                ('store_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.stores')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('quantity', models.IntegerField(null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(null=True)),
                ('sale', models.FloatField(null=True)),
                ('status', models.BooleanField(null=True)),
                ('datetime_create', models.DateTimeField()),
                ('price_total', models.FloatField(null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='Photo_products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('data', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluates',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rate', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.users')),
            ],
        ),
    ]
