# Generated by Django 3.2.7 on 2021-09-21 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio1',
            fields=[
                ('author_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.author')),
                ('text', models.CharField(max_length=64)),
            ],
            bases=('library.author',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('authors', models.ManyToManyField(to='library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
    ]
