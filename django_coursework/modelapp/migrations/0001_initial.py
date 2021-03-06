# Generated by Django 3.0.1 on 2020-02-10 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('student_class', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('student', models.ManyToManyField(blank=True, to='modelapp.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='modelapp.Teacher'),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='modelapp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('class_type', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='modelapp.Student')),
            ],
        ),
    ]
