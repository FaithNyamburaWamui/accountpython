# Generated by Django 5.0.6 on 2024-06-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_age', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=20)),
                ('teacher_id', models.IntegerField()),
                ('teacher_course', models.CharField(max_length=20)),
                ('teacher_class', models.CharField(max_length=20)),
                ('teacher_description', models.CharField(max_length=20)),
                ('teacher_occupation', models.CharField(max_length=20)),
                ('teacher_salary', models.IntegerField()),
                ('teacher_hobby', models.CharField(max_length=20)),
                ('teacher_gender', models.CharField(max_length=20)),
            ],
        ),
    ]