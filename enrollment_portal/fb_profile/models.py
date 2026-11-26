from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=120, default="Alex Mercer")
    bio = models.CharField(max_length=255, default="Building cool web apps with Django & Python 🚀")
    work = models.CharField(max_length=120, default="Software Developer at TechCorp")
    location = models.CharField(max_length=120, default="Manila, Philippines")
    friends_count = models.PositiveIntegerField(default=842)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.full_name
