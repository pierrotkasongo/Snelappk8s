# Generated by Django 4.2.3 on 2023-07-17 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_center', models.CharField(max_length=100)),
                ('address_center', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_subscriber', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('type_subscriber', models.CharField(max_length=50)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.center')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_invoice', models.DateField(auto_created=True, auto_now_add=True)),
                ('invoice_code', models.CharField(max_length=20, unique=True)),
                ('month', models.CharField(max_length=50)),
                ('index_invoice', models.CharField(max_length=50)),
                ('consommation', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Impayée', max_length=50)),
                ('souscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('registration_number', models.CharField(max_length=20, unique=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.center')),
            ],
        ),
    ]