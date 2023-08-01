# Generated by Django 4.0.5 on 2022-06-25 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_instructor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.volunteer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='class_volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.volunteer'),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.class'),
        ),
        migrations.CreateModel(
            name='tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_marks', models.PositiveIntegerField()),
                ('test_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.students')),
                ('test_volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.volunteer')),
            ],
        ),
    ]
