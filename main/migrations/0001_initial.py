# Generated by Django 4.1.7 on 2023-06-20 09:00

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144, verbose_name='name')),
                ('color', models.CharField(default='orange', max_length=50, verbose_name='color')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('group', models.CharField(max_length=255, verbose_name='group')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('time', models.CharField(max_length=20, verbose_name='time')),
                ('type', models.CharField(max_length=20, verbose_name='type')),
                ('cab', models.CharField(max_length=64, null=True, verbose_name='cab')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='name')),
                ('deadline', models.DateTimeField(null=True)),
                ('color', models.CharField(default='orange', max_length=50, verbose_name='color')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
