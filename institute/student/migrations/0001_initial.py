# Generated by Django 3.0.5 on 2023-08-01 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('overall_progress', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('Admmission_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcedamicsRemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_science', models.CharField(max_length=300)),
                ('mathematics', models.CharField(max_length=300)),
                ('algorithms', models.CharField(max_length=300)),
                ('database', models.CharField(max_length=300)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]