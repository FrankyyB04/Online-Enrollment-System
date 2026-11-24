from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "EnrollFlow Admin Panel"
admin.site.site_title = "EnrollFlow Enrollment System"
admin.site.index_title = "Class & Student Records Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]
