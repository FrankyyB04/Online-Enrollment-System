from django.contrib import messages
from django.db.models import Q, Avg
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import StudentRegistrationForm
from .models import Student


def student_directory(request):
    query = request.GET.get('q', '').strip()
    selected_section = request.GET.get('section', '').strip()
    selected_status = request.GET.get('status', '').strip()
    selected_id = request.GET.get('student', '').strip()

    all_students = Student.objects.all()
    sections = (
        Student.objects.values_list('class_section', flat=True)
        .distinct()
        .order_by('class_section')
    )

    students = all_students
    if selected_section:
        students = students.filter(class_section=selected_section)
    if selected_status:
        students = students.filter(enrollment_status=selected_status)
    if query:
        students = students.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(student_id__icontains=query)
            | Q(email__icontains=query)
            | Q(program__icontains=query)
        )

    active_student = None
    if selected_id:
        active_student = students.filter(id=selected_id).first()
    if active_student is None:
        active_student = students.first()

    avg_gpa = students.aggregate(avg=Avg('previous_gpa'))['avg']

    context = {
        'students': students,
        'active_student': active_student,
        'sections': sections,
        'selected_section': selected_section,
        'selected_status': selected_status,
        'query': query,
        'total_count': students.count(),
        'enrolled_count': students.filter(enrollment_status='Enrolled').count(),
        'pending_count': students.filter(enrollment_status='Pending Review').count(),
        'avg_gpa': round(avg_gpa, 2) if avg_gpa else None,
    }
    return render(request, 'students/dashboard.html', context)


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(
                request,
                f"{student.complete_full_name} ({student.student_id}) has been registered to {student.class_section}."
            )
            return redirect(f"{reverse('students:directory')}?student={student.id}")
    else:
        form = StudentRegistrationForm()

    existing_sections = (
        Student.objects.values_list('class_section', flat=True)
        .distinct()
        .order_by('class_section')
    )

    return render(request, 'students/register.html', {
        'form': form,
        'existing_sections': existing_sections,
    })
