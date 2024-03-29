# Generated by Django 5.0.1 on 2024-02-21 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('citizenship', models.CharField(max_length=255, verbose_name='Fuqarolik')),
                ('pass_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Passport raqami')),
                ('pass_date', models.DateField(null=True, verbose_name='Passport muddati')),
                ('jshshir', models.CharField(max_length=14, null=True)),
                ('country', models.CharField(max_length=255, verbose_name='Mamlakat')),
                ('village', models.CharField(blank=True, max_length=255, null=True, verbose_name='Viloyat')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='shahar/tuman')),
                ('birth_date', models.DateField(null=True, verbose_name="Tug'ilgan kun")),
                ('gender', models.CharField(max_length=35, verbose_name='Jinsi')),
                ('live_village', models.CharField(max_length=255, null=True, verbose_name='Yashayotgan Viloyati')),
                ('live_city', models.CharField(max_length=255, null=True, verbose_name='Yashayotgan shahar/tumani')),
                ('live_mfy', models.CharField(max_length=255, null=True, verbose_name='Yashayotgan MFY')),
                ('live_street', models.CharField(max_length=255, null=True, verbose_name="Ko'cha")),
                ('live_home', models.CharField(max_length=255, null=True, verbose_name='uy')),
                ('edu_country', models.CharField(blank=True, max_length=255, null=True)),
                ('edu_name', models.CharField(blank=True, max_length=255, null=True)),
                ('speciality', models.CharField(blank=True, max_length=255, null=True)),
                ('edu_degree', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': "O'qituvchilar",
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakultet', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('hours', models.IntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='main.employee')),
                ('teachgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_group', to='main.group')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('accept', 'qabul qilindi'), ('reject', 'qabul qilinmadi')], max_length=35)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='main.document')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='main.employee')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='main.teachergroup')),
            ],
            options={
                'unique_together': {('employee', 'document', 'group')},
            },
        ),
    ]
