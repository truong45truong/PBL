# Generated by Django 4.1.2 on 2022-11-14 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
                ('receiver', models.CharField(max_length=50, null=True)),
                ('address_receiver', models.CharField(max_length=200, null=True)),
                ('phone_receiver', models.CharField(max_length=10, null=True)),
                ('status', models.BooleanField()),
                ('total_price', models.FloatField(null=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Transports',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('allowed', models.BooleanField()),
                ('datetime', models.DateTimeField()),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detailorders', to='order.orders')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='transport_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.transports'),
        ),
        migrations.CreateModel(
            name='Detail_orders',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.orders')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.products')),
            ],
        ),
    ]
