# Generated by Django 2.0 on 2019-04-06 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cust_name', models.CharField(max_length=200)),
                ('Cust_address', models.TextField(max_length=200)),
                ('Cust_contact', models.CharField(max_length=200)),
                ('Cust_gender', models.CharField(max_length=200)),
                ('Cust_city_id', models.CharField(max_length=200)),
                ('Cust_country_id', models.CharField(max_length=200)),
                ('Cust_state_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('Orderdate', models.DateField(auto_now_add=True)),
                ('ordertime', models.TimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sp_name', models.CharField(max_length=200)),
                ('Sp_address', models.TextField(max_length=200)),
                ('Sp_contact', models.CharField(max_length=200)),
                ('Sp_gender', models.CharField(max_length=200)),
                ('Sp_country_id', models.CharField(max_length=200)),
                ('Sp_state_id', models.CharField(max_length=200)),
                ('Sp_city_id', models.CharField(max_length=200)),
                ('Sp_service', models.CharField(default='test', max_length=200)),
                ('Sp_sub', models.CharField(default='test', max_length=200)),
                ('profile_img', models.FileField(blank=True, default='set.jpg', null=True, upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubService_name', models.CharField(max_length=50)),
                ('Service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.Service_detail')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=459)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='service_provider',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.User'),
        ),
        migrations.AddField(
            model_name='order_info',
            name='Service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.Service_detail'),
        ),
        migrations.AddField(
            model_name='order_info',
            name='Sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.Sub_service'),
        ),
        migrations.AddField(
            model_name='order_info',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.User'),
        ),
        migrations.AddField(
            model_name='customer_detail',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.User'),
        ),
        migrations.AddField(
            model_name='allinfo',
            name='Service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.Service_detail'),
        ),
        migrations.AddField(
            model_name='allinfo',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicehub.Sub_service'),
        ),
    ]
