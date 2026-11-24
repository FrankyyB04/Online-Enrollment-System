from datetime import date
from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # Enrollment & Class Assignment
            'student_id',
            'program',
            'class_section',
            'year_level',
            'academic_term',
            'enrollment_status',
            'enrollment_date',
            'documents_verified',
            # Personal Information
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'gender',
            'nationality',
            'email',
            'phone_number',
            'home_address',
            'emergency_contact_name',
            'emergency_contact_relation',
            'emergency_contact_phone',
            # Background Information
            'previous_school',
            'school_type',
            'graduation_year',
            'previous_gpa',
            'honors_awards',
            'guardian_name',
            'guardian_occupation',
            'guardian_contact',
            'scholarship_status',
            'admin_notes',
        ]
        widgets = {
            'student_id': forms.TextInput(attrs={'placeholder': 'e.g., 2026-00301'}),
            'program': forms.TextInput(attrs={'placeholder': 'e.g., BS Information Technology'}),
            'class_section': forms.TextInput(attrs={'placeholder': 'e.g., BSIT 3-A'}),
            'year_level': forms.TextInput(attrs={'placeholder': 'e.g., 1st Year / 3rd Year'}),
            'academic_term': forms.TextInput(attrs={'placeholder': 'e.g., 1st Semester, AY 2026-2027'}),
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle name (optional)'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'e.g., Filipino'}),
            'email': forms.EmailInput(attrs={'placeholder': 'student@school.edu'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+63 9XX XXX XXXX'}),
            'home_address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Street, Barangay, City/Municipality, Province'}),
            'emergency_contact_name': forms.TextInput(attrs={'placeholder': 'Full name of emergency contact'}),
            'emergency_contact_relation': forms.TextInput(attrs={'placeholder': 'e.g., Mother, Father, Guardian'}),
            'emergency_contact_phone': forms.TextInput(attrs={'placeholder': '+63 9XX XXX XXXX'}),
            'previous_school': forms.TextInput(attrs={'placeholder': 'Name of previous high school or college'}),
            'graduation_year': forms.NumberInput(attrs={'min': 1990, 'max': 2030}),
            'previous_gpa': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'e.g., 1.45'}),
            'honors_awards': forms.TextInput(attrs={'placeholder': 'e.g., With Honors (optional)'}),
            'guardian_name': forms.TextInput(attrs={'placeholder': 'Parent or legal guardian full name'}),
            'guardian_occupation': forms.TextInput(attrs={'placeholder': 'Occupation (optional)'}),
            'guardian_contact': forms.TextInput(attrs={'placeholder': '+63 9XX XXX XXXX'}),
            'scholarship_status': forms.TextInput(attrs={'placeholder': 'e.g., Academic Scholar (50%) or Regular'}),
            'admin_notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Optional remarks about documents, transfer credits, or status...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.is_bound:
            self.initial.setdefault('student_id', self.generate_next_student_id())
            self.initial.setdefault('enrollment_date', date.today())
            self.initial.setdefault('enrollment_status', 'Enrolled')

    @staticmethod
    def generate_next_student_id():
        year_prefix = str(date.today().year)
        existing_ids = Student.objects.filter(
            student_id__startswith=f"{year_prefix}-"
        ).values_list('student_id', flat=True)
        max_seq = 100
        for sid in existing_ids:
            parts = sid.split('-')
            if len(parts) == 2 and parts[1].isdigit():
                max_seq = max(max_seq, int(parts[1]))
        return f"{year_prefix}-{max_seq + 1:05d}"

    def clean_student_id(self):
        return self.cleaned_data['student_id'].strip()

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()
