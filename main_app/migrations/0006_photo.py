# Generated by Django 4.2.1 on 2023-06-02 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_ship_crew'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ship')),
            ],
        ),
    ]
