# Generated by Django 3.2.13 on 2022-04-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airflow', '0002_alter_searchresult_search_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
