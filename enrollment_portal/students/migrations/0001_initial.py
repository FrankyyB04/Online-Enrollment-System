from datetime import date
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(help_text='e.g., 2026-00101', max_length=20, unique=True)),
                ('program', models.CharField(default='BS Information Technology', max_length=120)),
                ('class_section', models.CharField(default='BSIT 3-A', help_text='e.g., BSIT 3-A', max_length=50)),
                ('year_level', models.CharField(default='3rd Year', max_length=30)),
                ('academic_term', models.CharField(default='1st Semester, AY 2026-2027', max_length=60)),
                ('enrollment_status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Pending Review', 'Pending Review'), ('Conditional', 'Conditional')], default='Enrolled', max_length=25)),
                ('enrollment_date', models.DateField(default=date.today)),
                ('documents_verified', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(blank=True, max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Non-Binary', 'Non-Binary'), ('Prefer not to say', 'Prefer not to say')], default='Female', max_length=25)),
                ('nationality', models.CharField(default='Filipino', max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=25)),
                ('home_address', models.TextField()),
                ('emergency_contact_name', models.CharField(max_length=120)),
                ('emergency_contact_relation', models.CharField(default='Parent', max_length=50)),
                ('emergency_contact_phone', models.CharField(max_length=25)),
                ('previous_school', models.CharField(max_length=150)),
                ('school_type', models.CharField(choices=[('Public High School', 'Public High School'), ('Private High School', 'Private High School'), ('Science High School', 'Science High School'), ('Transfer / College', 'Transfer / College')], default='Public High School', max_length=40)),
                ('graduation_year', models.PositiveIntegerField(default=2024)),
                ('previous_gpa', models.DecimalField(decimal_places=2, help_text='e.g., 1.45 or 3.85', max_digits=4)),
                ('honors_awards', models.CharField(blank=True, default='With Honors', max_length=200)),
                ('guardian_name', models.CharField(max_length=120)),
                ('guardian_occupation', models.CharField(blank=True, max_length=100)),
                ('guardian_contact', models.CharField(max_length=25)),
                ('scholarship_status', models.CharField(default='Academic Scholar (50%)', max_length=100)),
                ('admin_notes', models.TextField(blank=True, help_text='Internal remarks visible to class administrators.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
