from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'full_name',
        'class_section',
        'program',
        'year_level',
        'enrollment_status',
        'documents_verified',
        'previous_gpa',
    )
    list_filter = (
        'class_section',
        'enrollment_status',
        'year_level',
        'documents_verified',
        'school_type',
    )
    search_fields = (
        'student_id',
        'first_name',
        'last_name',
        'email',
        'class_section',
        'previous_school',
    )
    list_editable = ('enrollment_status', 'documents_verified')
    ordering = ('class_section', 'last_name', 'first_name')

    fieldsets = (
        ('1. Enrollment & Class Assignment', {
            'fields': (
                ('student_id', 'enrollment_status'),
                ('program', 'class_section'),
                ('year_level', 'academic_term'),
                ('enrollment_date', 'documents_verified'),
            )
        }),
        ('2. Personal Information', {
            'fields': (
                ('first_name', 'middle_name', 'last_name'),
                ('date_of_birth', 'gender', 'nationality'),
                ('email', 'phone_number'),
                'home_address',
                ('emergency_contact_name', 'emergency_contact_relation', 'emergency_contact_phone'),
            )
        }),
        ('3. Educational & Family Background', {
            'fields': (
                ('previous_school', 'school_type'),
                ('graduation_year', 'previous_gpa', 'honors_awards'),
                ('guardian_name', 'guardian_occupation', 'guardian_contact'),
                'scholarship_status',
                'admin_notes',
            )
        }),
    )
