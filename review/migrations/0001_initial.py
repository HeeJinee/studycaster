# Generated by Django 2.2.3 on 2019-08-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('volume', models.CharField(choices=[('★★★★★', '★★★★★'), ('★★', '★★'), ('★', '★'), ('★★★★', '★★★★'), ('★★★', '★★★')], default='★', max_length=5)),
                ('runningtime', models.CharField(choices=[('★★★★★', '★★★★★'), ('★★', '★★'), ('★', '★'), ('★★★★', '★★★★'), ('★★★', '★★★')], default='★', max_length=5)),
                ('fun', models.CharField(choices=[('★★★★★', '★★★★★'), ('★★', '★★'), ('★', '★'), ('★★★★', '★★★★'), ('★★★', '★★★')], default='★', max_length=5)),
                ('total', models.CharField(choices=[('★★★★★', '★★★★★'), ('★★', '★★'), ('★', '★'), ('★★★★', '★★★★'), ('★★★', '★★★')], default='★', max_length=5)),
            ],
        ),
    ]
