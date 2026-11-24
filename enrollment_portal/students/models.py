from datetime import date
from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Non-Binary', 'Non-Binary'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Pending Review', 'Pending Review'),
        ('Conditional', 'Conditional'),
    ]

    SCHOOL_TYPE_CHOICES = [
        ('Public High School', 'Public High School'),
        ('Private High School', 'Private High School'),
        ('Science High School', 'Science High School'),
        ('Transfer / College', 'Transfer / College'),
    ]

    # Enrollment & Class Assignment
    student_id = models.CharField(max_length=20, unique=True, help_text="e.g., 2026-00101")
    program = models.CharField(max_length=120, default="BS Information Technology")
    class_section = models.CharField(max_length=50, default="BSIT 3-A", help_text="e.g., BSIT 3-A")
    year_level = models.CharField(max_length=30, default="3rd Year")
    academic_term = models.CharField(max_length=60, default="1st Semester, AY 2026-2027")
    enrollment_status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Enrolled')
    enrollment_date = models.DateField(default=date.today)
    documents_verified = models.BooleanField(default=True)

    # Personal Information
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default='Female')
    nationality = models.CharField(max_length=50, default="Filipino")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25)
    home_address = models.TextField()
    emergency_contact_name = models.CharField(max_length=120)
    emergency_contact_relation = models.CharField(max_length=50, default="Parent")
    emergency_contact_phone = models.CharField(max_length=25)

    # Background Information (Academic & Family)
    previous_school = models.CharField(max_length=150)
    school_type = models.CharField(max_length=40, choices=SCHOOL_TYPE_CHOICES, default='Public High School')
    graduation_year = models.PositiveIntegerField(default=2024)
    previous_gpa = models.DecimalField(max_digits=4, decimal_places=2, help_text="e.g., 1.45 or 3.85")
    honors_awards = models.CharField(max_length=200, blank=True, default="With Honors")
    guardian_name = models.CharField(max_length=120)
    guardian_occupation = models.CharField(max_length=100, blank=True)
    guardian_contact = models.CharField(max_length=25)
    scholarship_status = models.CharField(max_length=100, default="Academic Scholar (50%)")
    admin_notes = models.TextField(blank=True, help_text="Internal remarks visible to class administrators.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.student_id} - {self.full_name} ({self.class_section})"

    @property
    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name[0]}. {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    @property
    def complete_full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(p for p in parts if p)

    @property
    def initials(self):
        first = self.first_name[0].upper() if self.first_name else ""
        last = self.last_name[0].upper() if self.last_name else ""
        return f"{first}{last}"

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
