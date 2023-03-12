from django.db import models
from django.conf import settings

# Create your models here.
from django.urls import reverse


class ProfileCoach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_coach")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    gym_location = models.CharField(max_length=250, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', default='profile/default_profile.jpg')
    biography = models.TextField(max_length=1000, blank=True, null=True)
    instagram = models.URLField(max_length=100, blank=True, null=True)
    facebook = models.URLField(max_length=100, blank=True, null=True)
    youtube = models.URLField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('authors_blog', kwargs={'name': self.first_name})

    def __str__(self):
        return f'{self.first_name} {self.last_name} profile'
