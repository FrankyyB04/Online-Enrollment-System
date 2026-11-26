from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import ProfilePictureForm

def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('fb_profile:profile')
    else:
        form = ProfilePictureForm(instance=profile)

    return render(request, 'fb_profile/profile.html', {
        'profile': profile,
        'form': form,
    })
