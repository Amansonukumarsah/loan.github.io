# Generated by Django 3.2 on 2021-11-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_studentdetails_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('pdf1', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]